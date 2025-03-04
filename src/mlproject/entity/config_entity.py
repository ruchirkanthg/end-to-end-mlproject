from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class IngestionConfig:
    root_dir: Path 
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class ValidationConfig:
    root_dir: Path 
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict

@dataclass(frozen=True)
class TransformationConfig:
    root_dir: Path
    data_path: Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    objective: str
    eval_metric: str
    target_col: str

@dataclass(frozen=True)
class EvaluationConfig:
    root_dir: Path 
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str