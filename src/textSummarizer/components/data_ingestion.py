import os
import zipfile
import traceback
from pathlib import Path
import urllib.request as request
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from textSummarizer.entity import DataIngestionConfig



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with following info: \n{headers}")
        else:
            logger.info(f"file already exists of sie: {get_size(Path(self.config.local_data_file))}")
            
    
    
    def unzip_data(self):
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"Data extracted successfully to {unzip_path}")
        except Exception as e:
            logger.error(f"Failed to extract ZIP file: {e}")
            logger.debug(traceback.format_exc())

        
        