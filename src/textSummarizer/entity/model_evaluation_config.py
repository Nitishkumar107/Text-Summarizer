from dataclasses import dataclass
from pathlib import Path

@dataclass (frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path : Path
    model_path : Path
    tokenizer_path : Path   
    metric_file_name : Path