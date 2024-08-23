#Updating the components

import os
import urllib.request as request
import zipfile
from TextSummarizer_llm.logging import logger
from TextSummarizer_llm.utils.common import get_size
from pathlib import Path
from TextSummarizer_llm.entity import DataIngestionConfig

import zipfile
class DataIngestion:
    def __init__(self,config:DataIngestionConfig):#This will take dataingestion configuration mentioned above in this notebook
        self.config=config#initializing the config

    def download_file(self):#This will download the file from the given URL
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}  ")

    def extract_zip_file(self):#This will extract the zip file
        """
        zip_file_path: str
        Extracts the data into the data/splitted directory
        Function returns: None
        """
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)