# APP Dashboard - Build and Maintaince

## Step 1 - Build dockerfile:
### Set the docker-namespace & namespace
```sh
export DOCKER_REPO="adilsonsilvajr"

export DOCKER_PROJECTNAME="diabetes-app"

export DOCKER_VERSION="v0.0.1"
```
### Build docker file, push to dockerhub and update latest version
```sh
docker image build -t $DOCKER_REPO/$DOCKER_PROJECTNAME:$DOCKER_VERSION .

docker push $DOCKER_REPO/$DOCKER_PROJECTNAME:$DOCKER_VERSION

docker tag $DOCKER_REPO/$DOCKER_PROJECTNAME:$DOCKER_VERSION $DOCKER_REPO/$DOCKER_PROJECTNAME:latest

docker push $DOCKER_REPO/$DOCKER_PROJECTNAME:$DOCKER_VERSION:latest
```
## Step 2 - Running k8s .yaml in the cloud
Verify [here](https://github.com/AdilsonSilvaJr/jupyterstack/tree/master/k8s) how create, build and maintaince k8s in cloud

## Extra commands dockerfile:
### Run docker file
```sh
docker container run -d -it --privileged --name $DOCKER_PROJECTNAME -p 8000:80 $DOCKER_REPO/$DOCKER_PROJECTNAME:latest
```
### Open bash in container
```sh
docker exec -it $DOCKER_PROJECTNAME bash
```
### Stop container:
```sh
docker container stop $DOCKER_PROJECTNAME
```