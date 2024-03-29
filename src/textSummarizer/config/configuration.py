from textSummarizer.entity import (
    DataIngestionConfig, DataValidationConfig, 
    DataTransformationConfig, ModelTrainerConfig,
    ModelEvaluationConfig
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
        
        
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config['data_transformation']
        
        create_directories([Path(config['root_dir'])]) 
        
        
        return DataTransformationConfig(
            root_dir=Path(config['root_dir']),
            data_path=Path(config['data_path']),
            tokenizer_name=Path(config['tokenizer_name'])
        )
        
        
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config['model_trainer']
        params = self.params['TrainingArguments']
        
        create_directories([Path(config['root_dir'])])
        
        model_trainer_config = ModelTrainerConfig(
            root_dir=Path(config['root_dir']),
            data_path=Path(config['data_path']),
            model_ckpt=Path(config['model_ckpt']),
            num_train_epochs=params['num_train_epochs'],
            warmup_steps=params['warmup_steps'],
            per_device_train_batch_size=params['per_device_train_batch_size'],
            weight_decay=params['weight_decay'],
            logging_steps=params['logging_steps'],
            evaluation_strategy=params['evaluation_strategy'],
            eval_steps=params['eval_steps'],
            save_steps=params['save_steps'],
            gradient_accumulation_steps=params['gradient_accumulation_steps']
        )

        return model_trainer_config
    
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
       config = self.config['model_evaluation']
       
       return ModelEvaluationConfig(
            root_dir=Path(config['root_dir']),
            data_path=Path(config['data_path']),
            model_path=Path(config['model_path']),
            tokenizer_path=Path(config['tokenizer_path']),
            metric_file_name=Path(config['metric_file_name'])
       )