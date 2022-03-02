#!/bin/bash
mkdir -p dags logs plugins
chmod 777 dags logs plugins

docker-compose up airflow-init

