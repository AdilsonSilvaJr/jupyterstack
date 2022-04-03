#!/bin/bash
k3d cluster create jupyter-stacklabs --servers 1 --agents 1 -p "8080:30000@loadbalancer"

kubectl apply -f k8s/deployment.yaml

kubectl delete -f k8s/deployment.yaml

#kubectl exec -it name-pod env | grep API_URL


# docker image build -t adilsonsilvajr/diabetes-app:v0.0.1 .
# docker push adilsonsilvajr/diabetes-app:v0.0.1
# docker tag adilsonsilvajr/diabetes-app:v0.0.1 adilsonsilvajr/diabetes-app:latest
# docker push adilsonsilvajr/diabetes-app:latest



# docker image build -t adilsonsilvajr/diabetes-ml:v0.0.1 .
# docker push adilsonsilvajr/diabetes-ml:v0.0.1
# docker tag adilsonsilvajr/diabetes-ml:v0.0.1 adilsonsilvajr/diabetes-ml:latest
# docker push adilsonsilvajr/diabetes-ml:latest

gcloud container clusters get-credentials amiable-port-343414-gke --region us-central1

