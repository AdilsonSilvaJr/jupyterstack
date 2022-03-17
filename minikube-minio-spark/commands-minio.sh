#!/bin/bash
#install
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install minio bitnami/minio

#Uninstall
helm uninstall minio bitnami/minio

#user
kubectl get secret --namespace default minio -o jsonpath="{.data.root-user}" | base64 --decode

#password
kubectl get secret --namespace default minio -o jsonpath="{.data.root-password}" | base64 --decode
