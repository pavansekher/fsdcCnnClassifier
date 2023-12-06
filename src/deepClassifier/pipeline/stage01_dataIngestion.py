from deepClassifier.components.stage01_dataIngestion import DataIngestion
from deepClassifier.config import ConfigurationManager
from deepClassifier import logger



logger.info(" Data Ingestion is started ")
config=ConfigurationManager()
       
data_ingestion_config=config.get_data_ingestion_config()

data_ingestion = DataIngestion(config=data_ingestion_config)

data_ingestion.download_file()

data_ingestion.unzip_and_clean()

logger.info(" Data Ingestion is COmpleted :)  ")