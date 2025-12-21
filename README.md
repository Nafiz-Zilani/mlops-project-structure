# mlops-project-structure

# Setup the Packege Folder CMD

pip install -e .

# Automaticly create file structure with bash
chmod +x ./file-setup.sh
./file-setup.sh

# Or # Automaticly create file structure with python
python3 template.py

# DVC CMDs

1. dvc init
2. dvc add ./artifacts/data_ingestion/raw.csv
3. 