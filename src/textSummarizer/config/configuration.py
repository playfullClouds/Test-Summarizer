from textSummarizer.entity import (
    DataIngestionConfig, DataValidationConfig
)

from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories


class ConfigurationManager:
    def __init__(
        self,
        config_filepath: Path,  
        params_filepath: Path):  
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        create_directories([self.config['artifacts_root']])  # Adjusted based on actual usage
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config['data_ingestion']
        
        create_directories([Path(config['root_dir'])])  # Ensure directory is a Path object
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config['root_dir']),  # Ensure these are Path objects
            source_URL=config['source_URL'],
            local_data_file=Path(config['local_data_file']),
            unzip_dir=Path(config['unzip_dir'])
        )
        
        return data_ingestion_config
    
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config['data_validation']
        
        create_directories([Path(config['root_dir'])]) 
        
       
        return DataValidationConfig(
            root_path=Path(config['root_dir']),
            STATUS_FILE=config['STATUS_FILE'],
            ALL_REQUIRED_DATA=config['ALL_REQUIRED_DATA']
        
        )