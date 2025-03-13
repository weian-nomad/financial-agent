# trader.py
import json
from agent_base import BaseLLMAgent

class TraderAgent(BaseLLMAgent):
    def __init__(self):
        super().__init__('configs/trader_config.yaml')

    def decide(self, final_outlook: dict) -> dict:
        outlook_json = json.dumps(final_outlook)
        return self.run(final_outlook=outlook_json)
