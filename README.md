# DevOps - Playlist Recommendation System  

![Kubernetes](https://img.shields.io/badge/Kubernetes-✓-blue)  
![ArgoCD](https://img.shields.io/badge/ArgoCD-✓-orange)  
![MachineLearning](https://img.shields.io/badge/Machine%20Learning-✓-green)  

## Description  

This project was developed as part of the **Cloud Computing** course in the second semester of 2024 at the **Federal University of Minas Gerais (UFMG)**. It implements a playlist recommendation system based on machine learning. The solution is deployed in a **Kubernetes** environment, using **DevOps** and **MLOps** practices for continuous integration and delivery. The system analyzes Spotify datasets, generates association rules, and recommends personalized playlists to users.  

## Architecture  

The system architecture consists of:  

- **Machine Learning Backend**: Generates association rules and trains models.  
- **Frontend**: Exposes a REST API for recommendation queries.  
- **Persistent Volume**: Stores models and data shared between services.  
- **Kubernetes**: Orchestrates containers and system resources.  
- **ArgoCD**: Manages the continuous deployment of the application.  

## Project Structure  

```plaintext
/cloud_computing
│
├── /assets              # Datasets and music lists
│   ├── /datasets        # Datasets used to train the recommendation model
│   └── /musics_list     # List of songs used to simulate client-server communication
│
├── /client              # Code to simulate client requests
│   └── client.py        # Script to simulate client-server communication
│
├── /config              # Kubernetes configuration files for service deployment
│   ├── deployment.yaml  # Deployment definitions for Kubernetes
│   └── service.yaml     # Service definitions for Kubernetes
│
├── /frontend_container  # Container with the frontend and related deployment scripts
│   ├── Dockerfile       # Dockerfile for building the frontend container
│   ├── app.py           # Main logic of the frontend and REST API
│   └── requirements.txt # Dependencies for the frontend
│
├── /ml_container        # Container with the backend and machine learning logic
│   ├── Dockerfile       # Dockerfile for building the backend container
│   ├── playlist_recommender.py # Playlist recommendation logic
│   └── requirements.txt # Dependencies for the backend
│
└── README.md            # This file
```  

## Technologies  

- **Languages**: Python, Flask  
- **Tools**: Docker, Kubernetes, ArgoCD  
- **Machine Learning**: Association rules (Frequent Itemset Mining)  
- **Database**: Persistent Volume for data storage  

## Prerequisites  

Make sure you have the following tools installed:  

- [Docker](https://www.docker.com/get-started)  
- [Kubernetes](https://kubernetes.io/docs/setup/)  
- [ArgoCD](https://argo-cd.readthedocs.io/en/stable/)  
- [Python 3.8+](https://www.python.org/downloads/)  

## License  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.  
