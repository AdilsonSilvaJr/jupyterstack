FROM gcr.io/spark-operator/spark-py:v3.0.0

USER root:root

RUN mkdir -p /app

COPY Ingest_diabetes_notebook.py /app/

COPY ./jars /opt/spark/jars

WORKDIR /app

USER 1001