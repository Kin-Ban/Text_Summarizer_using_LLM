from TextSummarizer_llm.config.configuration import ConfigurationManager
from TextSummarizer_llm.components.model_evaluation import ModelEvaluation
from TextSummarizer_llm.logging import logger

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evaluation_config=ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()
                    
     
