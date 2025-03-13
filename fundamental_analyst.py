# fundamental_analyst.py
from agent_base import BaseLLMAgent

class FundamentalAnalystAgent(BaseLLMAgent):
    def __init__(self):
        super().__init__('configs/fundamental_analyst_config.yaml')

    def analyze(self, fundamental_data: str) -> dict:
        """
        回傳 { "score": float, "comment": str }
        """
        return self.run(fundamental_data=fundamental_data)
