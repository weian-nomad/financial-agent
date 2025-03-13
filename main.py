# main.py
from fundamental_analyst import FundamentalAnalystAgent
from news_analyst import NewsAnalystAgent
from sentiment_analyst import SentimentAnalystAgent
from technical_analyst import TechnicalAnalystAgent
from research_team import BullishResearcher, BearishResearcher, ResearchFacilitator
from trader import TraderAgent
from risk_manager import RiskManager, RiskFacilitator
from fund_manager import FundManager

def main():
    # 1) 分析師
    fundamental_agent = FundamentalAnalystAgent()
    news_agent = NewsAnalystAgent()
    sentiment_agent = SentimentAnalystAgent()
    technical_agent = TechnicalAnalystAgent()

    # 假設有些文本
    fundamental_data = "Revenue grew 10%, EPS up 15%, Debt/Equity=0.4..."
    news_data = "Company announced new AI product, market reaction positive."
    sentiment_data = "Social media hype about new AI technology, mostly bullish."
    technical_data = "RSI=65, MACD nearing golden cross, volume picking up."

    # 2) 分析師產生報告
    f_result = fundamental_agent.analyze(fundamental_data)
    n_result = news_agent.analyze(news_data)
    s_result = sentiment_agent.analyze(sentiment_data)
    t_result = technical_agent.analyze(technical_data)

    # 收集成一個 list
    analyst_reports = [
        {"agent": "Fundamental", "result": f_result},
        {"agent": "News", "result": n_result},
        {"agent": "Sentiment", "result": s_result},
        {"agent": "Technical", "result": t_result},
    ]

    # 3) 研究團隊
    bullish_agent = BullishResearcher()
    bearish_agent = BearishResearcher()
    facilitator = ResearchFacilitator()

    bull_view = bullish_agent.summarize(analyst_reports)
    bear_view = bearish_agent.summarize(analyst_reports)
    final_outlook = facilitator.conclude(bull_view, bear_view)
    print("Final Outlook:", final_outlook)

    # 4) 交易
    trader_agent = TraderAgent()
    trade_decision = trader_agent.decide(final_outlook)
    print("Trade Decision:", trade_decision)

    # 5) 風控
    portfolio = {"AAPL": 50}
    risk_manager = RiskManager()
    risk_result = risk_manager.evaluate(trade_decision, portfolio)
    print("Risk Result:", risk_result)

    risk_facilitator = RiskFacilitator()
    final_risk = risk_facilitator.finalize([risk_result])
    print("Final Risk Adjusted:", final_risk)

    # 6) 基金經理執行
    fund_manager = FundManager()
    updated_portfolio = fund_manager.execute(final_risk, portfolio)
    print("Updated Portfolio:", updated_portfolio)

if __name__ == "__main__":
    main()
