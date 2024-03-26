from pathlib import Path

from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger


CONFIG_FILE_PATH = Path('C:/Test-Summarizer/config/config.yaml')  
PARAMS_FILE_PATH = Path('C:/Test-Summarizer/params.yaml')



STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline(CONFIG_FILE_PATH, PARAMS_FILE_PATH)
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e