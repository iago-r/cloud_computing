import warnings
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules

def create_association_rules(df, min_support=0.01, min_threshold=0.5, metric="confidence", save_path=None):
    if not {'pid', 'track_name'}.issubset(df.columns):
        print("O DataFrame deve conter as colunas 'pid' e 'track_name'")
        return 1

    grouped = df.groupby('pid')['track_name'].apply(list)
    dataset = grouped.tolist()

    te = TransactionEncoder()
    te_ary = te.fit(dataset).transform(dataset)
    encoded_df = pd.DataFrame(te_ary, columns=te.columns_)

    frequent_itemsets = fpgrowth(encoded_df, min_support=min_support, use_colnames=True)

    rules = association_rules(
        frequent_itemsets, num_itemsets=len(df), metric=metric, min_threshold=min_threshold
    ).sort_values(by=metric, ascending=False)[['antecedents', 'consequents', 'support', 'confidence', 'lift']]

    if not save_path:
        print("Um caminho para salvar as regras deve ser fornecido")
        return 1;

    rules.to_pickle(save_path)
    return rules

df = pd.read_csv("arquivo.csv", delimiter=',') # troquei o delimiter ; porque aparentemente vem com , de fábrica
rules = create_association_rules(df, min_support=0.05, min_threshold=0.5, save_path='model.pkl')