# textSummarizer/components/data_validation.py

import os
from textSummarizer.logging import logger
from textSummarizer.entity.data_validation_config import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = True

            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))

            missing_files = [file for file in self.config.ALL_REQUIRED_FILES if file not in all_files]

            if missing_files:
                validation_status = False
                logger.error(f"Missing files: {missing_files}")
            else:
                logger.info("All required files are present.")

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            logger.error(f"An error occurred during file validation: {e}")
            raise e
