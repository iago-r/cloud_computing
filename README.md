# DevOps

### Pré-requisitos

- [Docker](https://www.docker.com/get-started)
- [Kubernetes](https://kubernetes.io/docs/setup/)
- [ArgoCD](https://argo-cd.readthedocs.io/en/stable/)
- [Python 3.8+](https://www.python.org/downloads/)

## Estrutura do Repositório

```
/cloud_computing
│
├── /assets              # Datasets e listas de músicas
│   ├── /datasets        # Datasets utilizados no treino das recomendações
│   └── /musics_list     # Lista de músicas utilizada para simular a comunicação do cliente com o servidor
│
├── /client              # Código do frontend
│   └── client.py        # Script para simular a comunicação do cliente com o servidor
│
├── /config              # Arquivos de configuração do Kubernetes para implantação dos serviços
│   ├── deployment.yaml  # Definições de deployment para Kubernetes
│   └── service.yaml     # Definições de serviço para Kubernetes
│
├── /frontend_container  # Container com o frontend e scripts relacionados à sua implantação
│   ├── Dockerfile       # Arquivo Dockerfile para a construção do container do frontend
│   ├── app.py           # Lógica principal do frontend e API REST
│   └── requirements.txt # Dependências para o frontend
│
├── /ml_container        # Container com o backend e a lógica de aprendizado de máquina
│   ├── Dockerfile       # Arquivo Dockerfile para a construção do container do backend
│   ├── playlist_recommender.py # Lógica de recomendação de playlists
│   └── requirements.txt # Dependências para o backend
│
└── README.md            # Este arquivo
```