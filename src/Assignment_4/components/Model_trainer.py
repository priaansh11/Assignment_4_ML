# components
import os
import numpy as np
import pandas as pd
from src.Assignment_4 import logger
from src.Assignment_4.utils.common import get_size
from src.Assignment_4.entity.config_entity import *
from sklearn.ensemble import AdaBoostClassifier
import joblib
from sklearn.tree import DecisionTreeClassifier


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)

        train_y = train_data[self.config.target_column]
        test_y = test_data[self.config.target_column]

        params = self.config.params.AdaBoostClassifier

        estimator1 = DecisionTreeClassifier(
        max_depth=params.estimator.max_depth,
        random_state=params.estimator.random_state
    )

        rf = AdaBoostClassifier(
            estimator= estimator1,
            n_estimators= params.n_estimators,       
            learning_rate= params.learning_rate,     
            random_state = params.random_state
        )

        rf.fit(train_x, train_y)

        joblib.dump(rf, os.path.join(self.config.root_dir, self.config.model_name))
