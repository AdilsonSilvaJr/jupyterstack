
# Airflow k8s - Instalation and Maintaince

Chart from: https://artifacthub.io/packages/helm/airflow-helm/airflow

## Step 1 - Add this helm repository:
### Add this helm repository & pull updates from it
```sh
helm repo add airflow-stable https://airflow-helm.github.io/charts

helm repo update
```
## Step 2 - Install chart:
### Set the release-name & namespace
```sh
export AIRFLOW_NAME="airflow-cluster"

export AIRFLOW_NAMESPACE="airflow-cluster"
```

### Create a local airflow cluster 
* Note: You have to installed "k3d" for continue
```sh
k3d cluster create $AIRFLOW_NAME --servers 1 --agents 1
```
### Create namespace
```sh
kubectl create ns $AIRFLOW_NAMESPACE
```
### Install using helm 3
* Note: Before install the .yaml file you have to change:
  - In gitSync - Line 1122 (repo:) - put your repository
  - In gitSync - Line 1128 (repoSubPath:) - put your dag location
```sh
helm install \
  $AIRFLOW_NAME \
  airflow-stable/airflow \
  --namespace $AIRFLOW_NAMESPACE \
  --version "8.X.X" \
  --values ./values-airflow.yaml
```
  
## Step 3 - Locally expose the airflow webserver:
### Port-forward the airflow webserver
```sh
kubectl port-forward svc/${AIRFLOW_NAME}-web 8080:8080 --namespace $AIRFLOW_NAMESPACE
```
* Open your browser to: [http://localhost:8080](http://localhost:8080)
* Default login: admin/admin

## Upgrade
### Pull updates from the helm repository
```sh
helm repo update
```
### Apply any new values // upgrade chart version to 8.X.X
```sh
helm upgrade \
  $AIRFLOW_NAME \
  airflow-stable/airflow \
  --namespace $AIRFLOW_NAMESPACE \
  --version "8.X.X" \
  --values ./custom-values.yaml
```  
  
## Uninstall
### Uninstall the chart
```sh
helm uninstall $AIRFLOW_NAME --namespace $AIRFLOW_NAMESPACE
```