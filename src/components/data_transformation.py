import os
import sys
import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from src.utils import save_object
from feast import Field, FeatureStore, Entity, FeatureView, FileSource
from feast.types import Float32, Int64, String
from feast.value_type import ValueType
from datetime import datetime, timedelta

@dataclass
class DataTransformationConfig:

    preprocess_obj_file_path = os.path.join("artifacts/data_transformation", "preprocessor.pkl")
    feature_store_repo_path = "feature_repo"

class DataTransformation:

    def __init__(self):
        try:
            self.data_transformation_config = DataTransformationConfig()

            #Get absolute path and creating the feature store directory structure
            repo_path = os.path.abspath(self.data_transformation_config.feature_store_repo_path)

            os.makedirs(os.path.join(repo_path, "data"), exist_ok=True)

            ## Create feature store yaml file with minimal configuration
            feature_store_yaml_path = os.path.join(repo_path, "feature_store.yaml")

            # Feature Store Confiuguration
            feature_store_yaml = """project: imcome_predictation
provider: local
registry: data/registry.db
online_store:
    type:sqlite
offline_store:
    type: file
entity_key_serialization_version: 2"""

            # Write Cofiguration file
            with open(feature_store_yaml_path, 'w') as f:
                f.write(feature_store_yaml)

            logging.info(f"Created feature store configuration at {feature_store_yaml_path}")

            # verify the configuration file contents

            with open (feature_store_yaml_path, 'r') as f:
                logging.info(f"Configure file content:\n{f.read()}")

            # Initialize the feature store
            self.feature_store = FeatureStore(repo_path=repo_path)
            logging.info("Feature Store initialized successfully")

        except Exception as e:

            logging.error(f"Error in the initialization{str(e)}")
            raise CustomException(e, sys)
        
    def get_data_transformation_obj(self):

        try:
            logging.info("Data Transformation has been started")

            numerical_feature = [
                'age',
                'workclass',
                'education_num',
                'marital_status',
                'occupation',
                'relationship',
                'race',
                'sex',
                'capital_gain',
                'capital_loss',
                'hours_per_week',
                'native_country'
            ]

            num_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )

            preprocessor = ColumnTransformer([
                ("num_pipeline", num_pipeline, numerical_feature)
            ])

            return preprocessor
        
        except Exception as e:

            # logging.error(f"Error in data transformation: {str(e)}")
            raise CustomException(e, sys)
        

    def remove_outliers_IQR(self, col, df): #Search IQR to handel Outliers Google

        try:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1

            lower_limit = Q1 - 1.5 * IQR
            upper_limit = Q3 + 1.5 * IQR
            
            df.loc[(df[col] > upper_limit), col] = upper_limit
            df.loc[(df[col] < lower_limit), col] = lower_limit

            return df
        
        except Exception as e:

            logging.error("Qutline handling processes are not working properly")
            raise CustomException(e, sys)
        
    def inittiate_data_transformation(self,  train_path, test_path):

        try:

            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            logging.info("Read train and test data completed")
            logging.info("Outlier processing object")

            preprocessing_obj = self.get_data_transformation_obj()

            target_coloum_name = "income"

            numerical_feature = [
                'age',
                'workclass',
                'education_num',
                'marital_status',
                'occupation',
                'relationship',
                'race',
                'sex',
                'capital_gain',
                'capital_loss',
                'hours_per_week',
                'native_country'
            ]

            input_feature_test_df = test_data.drop(columns=[target_coloum_name], axis=1)
            target_feature_test_df = test_data[target_coloum_name]

            logging.info("Applying Preprocessing object on training and testing datasets")

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_test_df)
            input_feature_test_arr = preprocessing_obj.fit_transform(input_feature_test_df)

            logging.info("Starting Feature Store Operations")

            # Push data to Feast Feature Store
            self.push_features_to_store(train_data, "train")

    def push_feature_to_store(self, df, entity_id):

        try:

            if 'event_timestamp' not in df.colums:
                df['event_timestamp'] = pd.Timestamp.now()

            if 'entity_id' not in df.colums:
                df['entity_id'] = range(len(df))

            data_path = os.path.join(self.data_transformation_config.feature_store_repo_path, 
                                     "data"
                                     )   #parquet format Google it
            
            parquet_path = os.path.join(data_path, f"{entity_id}_feature.parquet")
            os.makedirs(data_path, exist_ok=True)

            df.to_parquest(parquet_path, index=False)
            logging.info(f"Saved Feature Data to {parquet_path}")

            data_source = FileSource(
                path = f"data/{entity_id}_feature.parquet",
                timestamp_field="event_timestamp"
            )

            entity = Entity(
                name = "entity_id",
                value_type= ValueType.INT64,
                description="Entity ID"
            ) #7 - 52:53