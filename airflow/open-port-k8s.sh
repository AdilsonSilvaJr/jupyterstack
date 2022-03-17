#!/bin/bash
export AIRFLOW_NAME="airflow-cluster"
export AIRFLOW_NAMESPACE="airflow-cluster"

kubectl port-forward svc/${AIRFLOW_NAME}-web 8080:8080 --namespace $AIRFLOW_NAMESPACE
