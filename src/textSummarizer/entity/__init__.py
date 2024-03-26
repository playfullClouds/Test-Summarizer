from pathlib import Path
from typing import List
from dataclasses import dataclass



@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
    
    
@dataclass(frozen=True)
class DataValidationConfig:
    root_path: Path 
    STATUS_FILE: str
    ALL_REQUIRED_DATA: List[str]