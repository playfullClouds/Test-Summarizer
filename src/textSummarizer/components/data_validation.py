import os

from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            # Define validation status
            validation_status = None

            # Get list of all directories in the specified path
            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))

            # Check if each required directory exists
            for file in all_files:
                if file not in self.config.ALL_REQUIRED_DATA:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            logger.error(f"Failed to validate file: {e}")
            raise