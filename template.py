import os
from pathlib import Path
import logging

# format for creating log
logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

# allocating name of the project
project_name = "cnnCloud"

# creating the list of files which needed to be created for the whole process
list_of_files = [
    # folder and files

    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]

for filepath in list_of_files:
    # handles the backward slash and forward slash between python and windows
    filepath = Path( filepath)
    file_dir, file_name = os.path.split(filepath)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory; {file_dir} for the file: {file_name}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0 ) :
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{file_name} is already exists")

