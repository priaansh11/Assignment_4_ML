import os
import numpy as np
import pandas as pd
from src.Assignment_4 import logger
from src.Assignment_4.utils.common import get_size
from src.Assignment_4.entity.config_entity import *
from sklearn.model_selection import train_test_split


#update the component

import os
class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config


    def train_test_spliting(self):
        data = pd.read_csv(r"D:\Cdac_ML\Assignments\Assignment_4\artifacts\data_ingestion\airplane.csv")

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)