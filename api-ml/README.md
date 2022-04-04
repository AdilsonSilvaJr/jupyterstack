# API Machine Learning - Build and Maintaince

## Step 1 - Build dockerfile:
### Set the docker-namespace & namespace
```sh
export DOCKER_NAMESPACE="adilsonsilvajr/diabetes-ml"

export DOCKER_VERSION="v0.0.1"
```
### Build docker file, push to dockerhub and update latest version
```sh
docker image build -t $DOCKER_NAMESPACE:$DOCKER_VERSION .

docker push $DOCKER_NAMESPACE:$DOCKER_VERSION

docker tag $DOCKER_NAMESPACE:$DOCKER_VERSION $DOCKER_NAMESPACE:latest

docker push $DOCKER_NAMESPACE:$DOCKER_VERSION:latest
```
## Step 2 - Running k8s .yaml in the cloud
### Verify [here](https://github.com/AdilsonSilvaJr/jupyterstack/tree/master/k8s) how create, build and maintaince k8s in cloud

## Extra commands dockerfile:
### Run docker file
```sh
docker container run -d -it --privileged --name diabetes-ml -p 8000:80 $DOCKER_NAMESPACE:latest
```
### Open bash in container
```sh
docker exec -it diabetes-ml bash
```
### Stop container:
```sh
docker container run -d -it --privileged --name diabetes-ml -p 8000:80 $DOCKER_NAMESPACE:latest
```