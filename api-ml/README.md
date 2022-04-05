# API Machine Learning - Build and Maintaince

## Step 1 - Build dockerfile:
### Set the docker-namespace & namespace
```sh
export DOCKER_REPO="adilsonsilvajr"

export DOCKER_PROJECTNAME="diabetes-ml"

export DOCKER_VERSION="v0.0.1"
```
### Build docker file, push to dockerhub and update latest version
```sh
docker image build -t $(echo $DOCKER_REPO)/$(echo $DOCKER_PROJECTNAME):$(echo $DOCKER_VERSION) .

docker push $(echo $DOCKER_REPO)/$(echo $DOCKER_PROJECTNAME):$(echo $DOCKER_VERSION)

docker tag $(echo $DOCKER_REPO)/$(echo $DOCKER_PROJECTNAME):$(echo $DOCKER_VERSION) $(echo $DOCKER_REPO)/$(echo $DOCKER_PROJECTNAME):latest

docker push $(echo $DOCKER_REPO)/$(echo $DOCKER_PROJECTNAME):latest
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