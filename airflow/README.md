
# Airflow k8s - Instalation and Maintaince

Chart from: https://artifacthub.io/packages/helm/airflow-helm/airflow

## Step 1 - Add this helm repository:
### add this helm repository & pull updates from it
```sh
helm repo add airflow-stable https://airflow-helm.github.io/charts

helm repo update
```
## Step 2 - Install chart:
### set the release-name & namespace
```sh
export AIRFLOW_NAME="airflow-cluster"

export AIRFLOW_NAMESPACE="airflow-cluster"
```

### create a local airflow cluster 
#### note: You have to installed "k3d" for continue
```sh
k3d cluster create $AIRFLOW_NAME
```
### create namespace
```sh
kubectl create ns $AIRFLOW_NAMESPACE
```
### install using helm 3
```sh
helm install \
  $AIRFLOW_NAME \
  airflow-stable/airflow \
  --namespace $AIRFLOW_NAMESPACE \
  --version "8.X.X" \
  --values ./values-airflow.yaml
```
  
## Step 3 - Locally expose the airflow webserver:
### port-forward the airflow webserver
```sh
kubectl port-forward svc/${AIRFLOW_NAME}-web 8080:8080 --namespace $AIRFLOW_NAMESPACE
```
### open your browser to: [http://localhost:8080](http://localhost:8080)
### default login: admin/admin

## Upgrade
### pull updates from the helm repository
```sh
helm repo update
```
### apply any new values // upgrade chart version to 8.X.X
```sh
helm upgrade \
  $AIRFLOW_NAME \
  airflow-stable/airflow \
  --namespace $AIRFLOW_NAMESPACE \
  --version "8.X.X" \
  --values ./custom-values.yaml
```  
  
## Uninstall
### uninstall the chart
```sh
helm uninstall $AIRFLOW_NAME --namespace $AIRFLOW_NAMESPACE
```