#!/bin/bash
k3d cluster create jupyter-stacklabs --servers 1 --agents 1 -p "8080:30000@loadbalancer"

kubectl apply -f k8s/deployment.yaml

kubectl delete -f k8s/deployment.yaml

#kubectl exec -it name-pod env | grep API_URL
