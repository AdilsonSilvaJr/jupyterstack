#!/bin/bash
gcsfuse -o allow_other --implicit-dirs bucket-diabetes /app/datasets
streamlit run app.py