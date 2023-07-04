import os
import urllib.request as request
import zipfile
from cnnCloud import logger
from cnnCloud.utils.common import get_size
from cnnCloud.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file ):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} Downloading with follwong info: \n{headers} ")
        else:
            file_size = get_size(Path(self.config.local_data_file ))
            logger.info(f"{filename} already exists of size: {file_size}")

    def extact_zip_file(self):
        """ 
        zip_file_path : str
        Extracts the zip file into the data directory
        Functions returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            