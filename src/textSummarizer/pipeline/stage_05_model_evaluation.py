from textSummarizer.logging import logger

from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_evaluation import ModelEvaluation


class ModelEvaluationTrainingPipeline:
    def __init__(self, config_filepath, params_filepath):
        self.config_filepath = config_filepath
        self.params_filepath = params_filepath

    def main(self):
        config = ConfigurationManager(self.config_filepath, self.params_filepath)
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()