import os
import yaml
from textSummarizer.logging import logger
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """

    Args:
        path_to_yaml (Path): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file
        
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
        return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError(f"Empty yaml file: {path_to_yaml}")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): Ignore if multiple dirs is to be created. Default to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")
    

@ensure_annotations
def get_size(path: Path) -> str:
    """_summary_

    Args:
        path (Path): path of the file

    Returns:
        str: size in kb
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"