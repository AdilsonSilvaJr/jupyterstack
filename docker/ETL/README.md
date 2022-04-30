# Dags - Ingest data diabetes
I have create a Minio object storage for simulate a AWS s3 bucket and make ETL in Google cloud storage.

## Step 1 - Install Minio 
### Add this helm repository & pull updates from it
```sh
helm repo add bitnami https://charts.bitnami.com/bitnami

helm repo update
```
## Step 2 - Install chart:
### Set the release-name & namespace
```sh
export MINIO_NAME="minio"

export MINIO_NAMESPACE="minio"
```
### Create namespace
```sh
kubectl create ns $MINIO_NAME
```
### Install using helm 3
```sh
helm install \
  $MINIO_NAME \
  bitnami/minio \
  --namespace $MINIO_NAMESPACE \
  --version "11.X.X" \
  --values ./values.yaml
```
### Open port 9001
```sh
kubectl port-forward --namespace $MINIO_NAMESPACE svc/minio 9001:9001
```

########################################################################################################

## Step 1 - Build dockerfile:
### Set the docker-namespace & namespace
```sh
export DOCKER_REPO="adilsonsilvajr"

export DOCKER_PROJECTNAME="diabetes-etl"

export DOCKER_VERSION="v0.0.1"
```
### Build docker file, push to dockerhub and update latest version
```sh
docker image build -t $(echo $DOCKER_REPO)/$(echo $DOCKER_PROJECTNAME):$(echo $DOCKER_VERSION) .

docker push $(echo $DOCKER_REPO)/$(echo $DOCKER_PROJECTNAME):$(echo $DOCKER_VERSION)

docker tag $(echo $DOCKER_REPO)/$(echo $DOCKER_PROJECTNAME):$(echo $DOCKER_VERSION) $(echo $DOCKER_REPO)/$(echo $DOCKER_PROJECTNAME):latest

docker push $(echo $DOCKER_REPO)/$(echo $DOCKER_PROJECTNAME):latest
```

########################################################################################################

## Step 1 - Install spark-operator helm chart:
```sh
helm repo add spark-operator https://googlecloudplatform.github.io/spark-on-k8s-operator

kubectl create ns processing

helm install spark spark-operator/spark-operator --namespace processing
```
## Step 2 - Execute .yaml
```sh
kubectl apply -f etl.yaml -n processing
```


k3d cluster create jupyter-stack