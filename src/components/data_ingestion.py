import os, sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:

    train_data_path = os.path.join("artifacts/data_ingestion", "train.csv")
    test_data_path = os.path.join("artifacts/data_ingestion", "test.csv")
    raw_data_path = os.path.join("artifacts/data_ingestion", "raw.csv")

class DataIngestion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):

        logging.info("Data Ingestion started")
        try:
            logging.info("Start reading the dataset from local source using Pandas")
            data = pd.read_csv(os.path.join("data-source", "adult.csv"))
            logging.info("Dataset read successfully")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw data has been stored successfully")

            train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)
            logging.info("Raw data has been splitted into train and test sets")

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Data ingestion completed successfully")

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            logging.info("Error occurred in data ingestion stage")
            raise CustomException(e, sys)
        
if __name__ == "__main__":

    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()