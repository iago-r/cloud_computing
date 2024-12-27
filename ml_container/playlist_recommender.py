import os
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules


def create_association_rules(df, min_support=0.01, min_threshold=0.5, metric="confidence", save_path=None):
    try:
        if not {'pid', 'track_name'}.issubset(df.columns):
            raise ValueError("O DataFrame deve conter as colunas 'pid' e 'track_name'")

        if not save_path:
            raise ValueError("Um caminho para salvar as regras deve ser fornecido")

        grouped = df.groupby('pid')['track_name'].apply(list)
        dataset = grouped.tolist()

        te = TransactionEncoder()
        te_ary = te.fit(dataset).transform(dataset)
        encoded_df = pd.DataFrame(te_ary, columns=te.columns_)

        frequent_itemsets = fpgrowth(encoded_df, min_support=min_support, use_colnames=True)

        rules = association_rules(
            frequent_itemsets, num_itemsets=len(df), metric=metric, min_threshold=min_threshold
        ).sort_values(by=metric, ascending=False)[['antecedents', 'consequents', 'support', 'confidence', 'lift']]

        rules.to_pickle(save_path)
        print(f"Regras salvas com sucesso em {save_path}")
    
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    dataset_url = os.getenv("DATASET_URL")
    
    if dataset_url is None:
        raise ValueError("A variável de ambiente não está definida.")
    
    df = pd.read_csv(dataset_url, delimiter=',') # troquei o delimiter ';' para ','
    create_association_rules(df, min_support=0.05, min_threshold=0.5, save_path='models/model.pkl')