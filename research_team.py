# research_team.py
import json
from agent_base import BaseLLMAgent

class BullishResearcher(BaseLLMAgent):
    def __init__(self):
        super().__init__('configs/bullish_research_config.yaml')

    def summarize(self, analyst_reports: list) -> dict:
        # 將多份分析報告轉成 JSON 傳給 Prompt
        reports_json = json.dumps(analyst_reports)
        return self.run(analyst_reports=reports_json)

class BearishResearcher(BaseLLMAgent):
    def __init__(self):
        super().__init__('configs/bearish_research_config.yaml')

    def summarize(self, analyst_reports: list) -> dict:
        reports_json = json.dumps(analyst_reports)
        return self.run(analyst_reports=reports_json)

class ResearchFacilitator(BaseLLMAgent):
    def __init__(self):
        super().__init__('configs/research_facilitator_config.yaml')

    def conclude(self, bull_result: dict, bear_result: dict) -> dict:
        # bull_result 和 bear_result 可能是 dict，其內有多頭/空頭論點
        bull_str = json.dumps(bull_result)
        bear_str = json.dumps(bear_result)
        return self.run(bullish_json=bull_str, bearish_json=bear_str)
