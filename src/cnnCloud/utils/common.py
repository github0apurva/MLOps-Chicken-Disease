import os
from box.exceptions import BoxValueError
import yaml
from cnnCloud import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox :
    """reads yaml file and resturnes
    
    Args:
    path_to_yaml (Path): path to yaml file
    
    Raises:
        ValueError: if yaml file is empty
        e: empty yaml file
        
    Returns:
        ConfigBox: ConfigBox object
    
    """
    try:
        with open(path_to_yaml, 'r') as f:
            content = yaml.safe_load(f)
            logger.info(f"read_yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
    
@ensure_annotations
def create_directories(path_to_dir:list, verbose = True):
    """create list of directories
    Args:
        path_to_dir (list): list of path of directories
        ignore_log (bool, optional ): whether to ignore, default to False.   
    """

    for path in path_to_dir:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory: {path}")


@ensure_annotations
def save_json(path_to_json:Path, data : dict) :
    """save json

    Args:
        path_to_json (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path_to_json, 'w') as f:
        json.dump(data, f, indent = 4 )

    logger.info(f"json file saved at : {path_to_json}") 


@ensure_annotations
def load_json(path_to_json:Path ) -> ConfigBox   :
    """load json file data

    Args:
        path_to_json (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dictionary
    """
    with open(path_to_json) as f:
        content = json.load(f)

    logger.info(f"json file loaded successfuly from : {path_to_json}") 
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any, path:Path) :
    """ save binary file

    Args:
        data (Any): data to be saved as binary file
        path (Path): path to save binary file    
    
    """
    joblib.dump(value = data, filename = path)
    logger.info(f"bin file saved successfully at : {path}") 


@ensure_annotations
def load_bin(path: Path) -> Any :
    """ load binary file

    Args:
        path: Path to binary file

    Returns:
        Any :Object stored in the file

    """

    data = joblib.load(path)    
    logger.info(f"bin file loaded successfully at : {path}")
    return data


@ensure_annotations
def get_size(path:Path) -> str:
    """ gey size in KB
    Args:
        path (Path): path of the file

    rerurns:
        str: return size in kb

    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kb} KB"

def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageBase64(croppedImagePath) :
    with open(croppedImagePath, 'rb') as f:
        return base64.b64encode(f.read())


