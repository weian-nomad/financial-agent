# fund_manager.py
import json
from agent_base import BaseLLMAgent

class FundManager(BaseLLMAgent):
    def __init__(self):
        super().__init__('configs/fund_manager_config.yaml')

    def execute(self, approved_trade: dict, current_portfolio: dict) -> dict:
        trade_json = json.dumps(approved_trade)
        port_json = json.dumps(current_portfolio)
        return self.run(approved_trade=trade_json, current_portfolio=port_json)
