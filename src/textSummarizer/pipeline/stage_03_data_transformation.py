from textSummarizer.logging import logger

from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransformation


class DataTransformationTrainingPipeline:
    def __init__(self, config_filepath, params_filepath):
        self.config_filepath = config_filepath
        self.params_filepath = params_filepath

    def main(self):
        config = ConfigurationManager(self.config_filepath, self.params_filepath)
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()