import os
import numpy as np
import pandas as pd
from src.Assignment_4 import logger
from src.Assignment_4.utils.common import get_size
from src.Assignment_4.entity.config_entity import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_spliting(self):

        data = pd.read_csv(self.config.data_path)

        target_col = "satisfaction" 

        train_df, test_df = train_test_split(data, test_size=0.2, random_state=42)

        X_train = train_df.drop(columns=[target_col])
        y_train = train_df[target_col]

        X_test = test_df.drop(columns=[target_col])
        y_test = test_df[target_col]

        # CATEGORICAL ENCODING
       
        cat_cols = ['Gender', 'Customer Type', 'Type of Travel', 'Class']

        ohe = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
        ohe.fit(X_train[cat_cols])

        X_train_ohe = pd.DataFrame(
            ohe.transform(X_train[cat_cols]),
            columns=ohe.get_feature_names_out(cat_cols),
            index=X_train.index
        )

        X_test_ohe = pd.DataFrame(
            ohe.transform(X_test[cat_cols]),
            columns=ohe.get_feature_names_out(cat_cols),
            index=X_test.index
        )

        # Merge OHE + numerical
        X_train_enc = pd.concat([X_train.drop(columns=cat_cols), X_train_ohe], axis=1)
        X_test_enc = pd.concat([X_test.drop(columns=cat_cols), X_test_ohe], axis=1)

        # Align features
        X_train_enc, X_test_enc = X_train_enc.align(X_test_enc, join="outer", axis=1, fill_value=0)

    
        # SCALING NUMERIC COLUMNS
        
        num_cols = X_train_enc.select_dtypes(include=["int64", "float64"]).columns

        scaler = StandardScaler()
        scaler.fit(X_train_enc[num_cols])

        X_train_enc[num_cols] = scaler.transform(X_train_enc[num_cols])
        X_test_enc[num_cols] = scaler.transform(X_test_enc[num_cols])

        # FINAL MERGE + SAVE
        
        train_final = pd.concat([X_train_enc, y_train], axis=1)
        test_final = pd.concat([X_test_enc, y_test], axis=1)

        # Save files
        train_path = os.path.join(self.config.root_dir, "train.csv")
        test_path = os.path.join(self.config.root_dir, "test.csv")

        train_final.to_csv(train_path, index=False)
        test_final.to_csv(test_path, index=False)

        logger.info("Train & Test transformed and saved successfully.")
        logger.info(f"Train shape: {train_final.shape}")
        logger.info(f"Test  shape: {test_final.shape}")

        print("Final train:", train_final.shape)
        print("Final test:", test_final.shape)
