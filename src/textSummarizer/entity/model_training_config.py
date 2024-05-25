from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps : int
    save_steps: int
    gradient_accumulation_steps: int

