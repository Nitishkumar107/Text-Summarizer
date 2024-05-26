from src.textSummarizer.pipeline.stage_01_data_ingestionPipeline import DataIngestionTrainingPipeline
from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_02_data_validation_pipeline import DataValidationTrainingPipeline

from src.textSummarizer.pipeline.stage_03_data_transformation_pipeline import DataTransformationTrainingPipeline
from src.textSummarizer.pipeline.stage_04_data_training_Pipeline import DataTrainerTrainingPipeline
from src.textSummarizer.pipeline.stage_05_model_evaluation_Pipeline import DataEvaluationTrainingPipeline



'''

STAGE_NAME = "Data Ingestion stage"
try:

    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e






STAGE_NAME = "Data validation stage"
try:

    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e




STAGE_NAME = "Data transformation stage"
try:

    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_transformatin = DataTransformationTrainingPipeline()
    data_transformatin.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Model Training stage"
try:

    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    Model_trainer = DataTrainerTrainingPipeline()
    Model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



'''

STAGE_NAME = "Model Evaluation stage"
try:

    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    Model_trainer = DataEvaluationTrainingPipeline()
    Model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e








