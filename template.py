import os

def create_files_and_directories(file_list):

    """
    Docstring for create_files_and_directories
    
    :param file_list: Description
    """

    for filepath in file_list:
        filedir = os.path.dirname(filepath)
        filename = os.path.basename(filepath)

        #Create the dir if it don't exist
        if filedir and not os.path.isdir(filedir):
            os.makedirs(filedir)
            print(f"Creating directory: {filedir} for the file {filename}")

        #Create the file if it don't exist
        if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
            open(filepath, 'a').close()
            print(f"Creating empty file: {filepath}")
        else:
            print(f"File already exists: {filepath}")

#List of files and directories to be created
list_of_files=[
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_monitoring.py",
    "src/pipelines/__init__.py",
    "src/pipelines/training_pipeline.py",
    "src/pipelines/prediction_pipeline.py",
    "src/exception.py", #Any Exception raised in the codebase will be handled here
    "src/logger.py", #To save logs
    "src/utils.py", #Common funcations used across the project
    "main.py"
]

create_files_and_directories(list_of_files)