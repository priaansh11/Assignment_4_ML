# components
import os
import numpy as np
import pandas as pd
from src.Assignment_4 import logger
from src.Assignment_4.utils.common import get_size
from src.Assignment_4.entity.config_entity import *


class DataValidation:
    def __init__(self, config : DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            data = pd.read_csv(r"D:\Cdac_ML\Assignments\Assignment_4\artifacts\data_ingestion\airplane1.csv")
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e
        