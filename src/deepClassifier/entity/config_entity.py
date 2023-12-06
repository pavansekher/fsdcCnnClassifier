from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    Source_URL:str
    local_date_file:Path
    unzip_dir:Path

