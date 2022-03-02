mkdir -p server-jupyter
docker container run -d --rm --name jupterserver -v $(pwd)/server-jupyter:/ds -p 8888:8888 adilsonsilvajr/dsimage
docker container logs jupterserver
