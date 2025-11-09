#pipeline
from src.Assignment_4.constants import *
from src.Assignment_4.utils.common import read_yaml, create_directories
from src.Assignment_4.entity.config_entity import *
from src.Assignment_4.config.configuration import *
from src.Assignment_4.components.Model_evaluation import *

STAGE_NAME = "Model evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.save_results()