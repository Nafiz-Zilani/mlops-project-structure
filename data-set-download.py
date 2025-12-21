import kagglehub
import shutil
import os

# Kaggle dataset ID
DATASET_ID = "uciml/adult-census-income"

# Target directory inside your project
TARGET_DIR = "data-source"

# Download dataset (goes to kagglehub cache)
dataset_path = kagglehub.dataset_download(DATASET_ID)

# Ensure target directory exists
os.makedirs(TARGET_DIR, exist_ok=True)

# Copy dataset into your project folder
shutil.copytree(dataset_path, TARGET_DIR, dirs_exist_ok=True)

print("Dataset downloaded and copied to:", os.path.abspath(TARGET_DIR))