from dataclasses import dataclass
from pathlib import Path
from typing import List

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: List[str]
