#!/bin/bash
#gcsfuse -o allow_other --implicit-dirs bucket-diabetes-ml /ml/model
uvicorn diabetes_ML:app --host 0.0.0.0 --port 80