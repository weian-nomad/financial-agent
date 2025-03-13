# news_analyst.py
from agent_base import BaseLLMAgent

class NewsAnalystAgent(BaseLLMAgent):
    def __init__(self):
        super().__init__('configs/news_analyst_config.yaml')

    def analyze(self, news_text: str) -> dict:
        return self.run(news_text=news_text)
