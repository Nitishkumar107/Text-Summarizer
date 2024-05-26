

from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_trainer import ModelTrainer
from textSummarizer.logging import logger
from textSummarizer.components.model_evaluation import ModelEvaluation


class DataEvaluationTrainingPipeline:
    def __init__(self):
        pass

    try:
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config= ModelEvaluation(config = model_evaluation_config)
        model_evaluation_config.evaluate()
    except Exception as e:
            raise e









