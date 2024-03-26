from textSummarizer.logging import logger

from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValidation







class DataValidationTrainingPipeline:
    def __init__(self, config_filepath, params_filepath):
        self.config_filepath = config_filepath
        self.params_filepath = params_filepath

    def main(self):
        config_manager = ConfigurationManager(self.config_filepath, self.params_filepath)
        data_validation_config = config_manager.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        validation_status = data_validation.validate_all_files_exist()
        print(f"Data validation status: {validation_status}")