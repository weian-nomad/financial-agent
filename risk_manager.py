# risk_manager.py
import json
from agent_base import BaseLLMAgent

class RiskManager(BaseLLMAgent):
    def __init__(self):
        super().__init__('configs/risk_manager_config.yaml')

    def evaluate(self, trade_decision: dict, portfolio: dict) -> dict:
        trade_json = json.dumps(trade_decision)
        port_json = json.dumps(portfolio)
        return self.run(trade_json=trade_json, portfolio_json=port_json)

class RiskFacilitator(BaseLLMAgent):
    def __init__(self):
        super().__init__('configs/risk_facilitator_config.yaml')

    def finalize(self, risk_outputs: list) -> dict:
        # risk_outputs 可能是多個 RiskManager 結果的列表
        data_json = json.dumps(risk_outputs)
        return self.run(risk_data=data_json)
