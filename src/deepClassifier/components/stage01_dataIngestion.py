
import os
import urllib.request as request
from zipfile import ZipFile

from deepClassifier.utils import utils
from deepClassifier import logger
from pathlib import Path

from deepClassifier.entity import DataIngestionConfig



from tqdm import tqdm

class DataIngestion:

    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_file(self):
        pass

    def get_update_list_of_file(self):
        pass

    def preprocess(self):
        pass

    def unzip_and_clean(self):
        pass
