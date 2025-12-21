#!/bin/bash

# This script sets up the necessary file structure for the project.
list_of_files=(
    "src/__init__.py"
    "src/components/__init__.py"
    "src/components/data_ingestion.py"
    "src/components/data_transformation.py"
    "src/components/model_trainer.py"
    "src/components/model_monitoring.py"
    "src/pipelines/__init__.py"
    "src/pipelines/training_pipeline.py"
    "src/pipelines/prediction_pipeline.py"
    "src/exception.py" #Any Exception raised in the codebase will be handled here
    "src/logger.py" #To save logs
    "src/utils.py" #Common funcations used across the project
    "main.py"
)

for filepath in "${list_of_files[@]}"; do
    filedir=$(dirname "$filepath")
    filename=$(basename "$filepath")

    if [ ! -d "$filedir" ] && [ "$filedir" != "." ]; then
        mkdir -p "$filedir"
        echo "Created directory: $filedir" for the file $filename
    fi

    if [ ! -e "$filepath" ] || [ ! -s "$filepath" ]; then
        touch "$filepath"
        echo "Create empthy file: $filepath"
    else
        echo "$filename already exists"
    fi
done