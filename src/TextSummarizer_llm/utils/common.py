#Suppose you need a function which you will use frequently in your entire code so instead of writting the entire function everytime you can create the function in this common.py file in utilis and then import this file whenever required

import os
from box.exceptions import BoxValueError
import yaml
from TextSummarizer_llm.logging import logger
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
from box import ConfigBox#

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns all the content present in it

    Args:
        path_to_yaml (Path): path like input

    Raises:
        e: if any other error occurs
        BoxValueError: if yaml file is empty
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as exc:
        raise ValueError("YAML file is empty") from exc
    except Exception as exc:
        raise exc
    
@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):

    """ creates directories from a list of paths
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """get the size of a file

    Args:
        path (Path): path of the file

    Returns:
        str: size of the file
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

    