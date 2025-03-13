# sentiment_analyst.py
from agent_base import BaseLLMAgent

class SentimentAnalystAgent(BaseLLMAgent):
    def __init__(self):
        super().__init__('configs/sentiment_analyst_config.yaml')

    def analyze(self, sentiment_data: str) -> dict:
        return self.run(sentiment_data=sentiment_data)
