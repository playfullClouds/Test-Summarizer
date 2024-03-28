from textSummarizer.logging import logger

from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_trainer import ModelTrainer


class ModelTrainerTrainingPipeline:
    def __init__(self, config_filepath, params_filepath):
        self.config_filepath = config_filepath
        self.params_filepath = params_filepath

    def main(self):
        config_manager = ConfigurationManager(self.config_filepath, self.params_filepath)
        model_trainer_config = config_manager.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()