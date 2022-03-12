#!/bin/bash
kubectl create ns airflow-jupyter
helm install airflow-jupyter -f values-airflow.yaml bitnami/airflow

#wait up all containers
#kubectl port-forward --namespace default svc/airflow-jupyter 8080:8080
#export AIRFLOW_PASSWORD=$(kubectl get secret --namespace "default" airflow-jupyter -o jsonpath="{.data.airflow-password}" | base64 --decode)
#echo User:user
#echo Password: $AIRFLOW_PASSWORD

#some commands
#minikube delete --all
