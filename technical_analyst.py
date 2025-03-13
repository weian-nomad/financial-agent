# technical_analyst.py
from agent_base import BaseLLMAgent

class TechnicalAnalystAgent(BaseLLMAgent):
    def __init__(self):
        super().__init__('configs/technical_analyst_config.yaml')

    def analyze(self, technical_data: str) -> dict:
        return self.run(technical_data=technical_data)
