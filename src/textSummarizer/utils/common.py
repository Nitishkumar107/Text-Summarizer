# here we will write our all utility functions each function will be independent and will have their own task 
# there functions will be defined in the other modules, packages and functions

import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logging
from ensure import ensure_annotations   # ensure library make sure for correct data format
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations                 # decorator ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    This function will read the yaml file and return the config box
    Args: path_to_yaml(str): path like input
    Raises: 
        BoxValueError: if yaml file is empty
        e: empty file
    return: 
        config box: configBox type

    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully") 
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")  
    except Exception as e:
        raise e


@ensure_annotations
def get_size(path:Path)-> str:
    """
    get size in KB

    Args: 
        path (Path): Path of the file

    Returns:
            str: size of the file in KB

    """
    size = os.path.getsize(path)
    return str(round(size/1024,2))+" KB"


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):    
    """ Create list of directories
    Args: path_to_directories ( list): list of path directories
    ignore_log(bool, optional): ignore if multiple directories is to be created. Default to False
    
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logging.info(f"directories created successfully at {path} ")











