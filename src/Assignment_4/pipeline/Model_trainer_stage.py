#pipeline
from src.Assignment_4.constants import *
from src.Assignment_4.utils.common import read_yaml, create_directories
from src.Assignment_4.entity.config_entity import *
from src.Assignment_4.config.configuration import *
from src.Assignment_4.components.Model_trainer import *

STAGE_NAME = "Model Trainer Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_tr_config = ModelTrainer(config=model_trainer_config)
        model_tr_config.train()