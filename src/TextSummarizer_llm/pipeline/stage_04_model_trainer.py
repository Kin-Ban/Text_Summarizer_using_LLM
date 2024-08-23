from TextSummarizer_llm.config.configuration import ConfigurationManager
from TextSummarizer_llm.components.model_trainer import ModelTrainer
from TextSummarizer_llm.logging import logger

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
                
     
