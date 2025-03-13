# 多代理人美股科技股決策系統

This project demonstrates how to use the multi-agent (Multi-Agent) architecture and large language models (LLM) to perform **US tech stock** data analysis, investment research, and trading decision-making. The project includes the following features:

1. **分析師團隊 (Analyst Agents)**：  
   - **基本面分析**(Fundamental)  
   - **新聞分析**(News)  
   - **情緒分析**(Sentiment)  
   - **技術分析**(Technical)  
   這些分析師負責處理不同面向的資料，輸出結構化分析結果。

2. **研究團隊 (Research Agents)**：  
   - **多頭研究員**(Bullish)  
   - **空頭研究員**(Bearish)  
   - **研究協調員**(Facilitator)  
   透過多頭/空頭論點的對比與協調，最終得出「Bullish/Bearish/Neutral」展望。

3. **交易與風控 (Trader & Risk)**：  
   - **交易員**(Trader)：根據展望決定下單  
   - **風險管理員**(RiskManager) / **風控協調員**(RiskFacilitator)：檢查風控規範，整合多方建議  
   - **基金經理**(FundManager)：最終執行交易並更新投資組合

所有代理人皆繼承自同一個基底類別 (`BaseLLMAgent`)，並且各自的 **Prompt** 與 **模型參數** 都定義在 `configs/` 目錄下的 YAML 文件中，方便維護與更新。

---

## Project structure

```
project/
├── agent_base.py                     # 共同基底類別 (BaseLLMAgent)
├── fundamental_analyst.py           # 基本面分析師
├── news_analyst.py                  # 新聞分析師
├── sentiment_analyst.py             # 情緒分析師
├── technical_analyst.py             # 技術分析師
├── research_team.py                 # 多頭/空頭研究員 & 研究協調員
├── trader.py                        # 交易員
├── risk_manager.py                  # 風險管理員 & 風控協調員
├── fund_manager.py                  # 基金經理
├── main.py                          # 範例執行流程
└── configs/
    ├── fundamental_analyst_config.yaml
    ├── news_analyst_config.yaml
    ├── sentiment_analyst_config.yaml
    ├── technical_analyst_config.yaml
    ├── bullish_research_config.yaml
    ├── bearish_research_config.yaml
    ├── research_facilitator_config.yaml
    ├── trader_config.yaml
    ├── risk_manager_config.yaml
    ├── risk_facilitator_config.yaml
    └── fund_manager_config.yaml
```

1. **`agent_base.py`**：定義了所有代理人共同使用的函式（載入 YAML、呼叫 LLM、解析 JSON 等）。  
2. **各分析師檔案**：實作 `analyze()`，處理特定領域資料 (財報/新聞/情緒/技術)。  
3. **`research_team.py`**：多頭研究員、空頭研究員、研究協調員，各自處理多角度意見整合。  
4. **交易與風控**：`trader.py` / `risk_manager.py` / `fund_manager.py`，分別執行下單、檢查風險與最終交易執行。  
5. **`configs/*.yaml`**：各代理人的 Prompt 模板與 LLM 參數配置。

---

## Setup and run

1. **安裝 Python 相依套件**
   ```bash
   pip install -r requirements.txt
   ```

2. **確保已安裝/部署 LLM**  
   - 預設使用 [Ollama](https://github.com/jmorganca/ollama) 與對應的模型，請依需求安裝或替換成其他 LLM API（例如 OpenAI）。

3. **執行測試流程**  
   ```bash
   python main.py
   ```
   此程式會:
   - 依序呼叫各分析師進行資料分析  
   - 讓研究團隊整合多空觀點  
   - 使用交易員與風控檢查  
   - 最後由基金經理執行並更新組合

4. **檢視輸出**  
   - 於終端機可看到每個代理人輸出的 JSON 結果，如 { "score": 0.8, "comment": "xxx" }，以及最終交易決策、更新後的投資組合等。

---

## key features

- **Prompt 配置化**：所有 Prompt 寫在 YAML 檔，工程師可無痛調整代理人的行為，不需改動程式。
- **多代理人協同**：分析師-研究員-交易員-風險管理，各司其職並透過 JSON 交換資訊，簡化流程整合。
- **模組化設計**：新增加如「ESG 分析師」或「併購分析師」的代理人時，僅需新增對應檔案與 YAML。
- **風險控管**：在交易決策前，由 RiskManager 與 FundManager 多層檢查，避免過度槓桿或單一標的暴露。
- **LLM 驅動**：結合大型語言模型，以自然語言方式解析新聞、財報、社群情緒等複雜文本資訊。

---

## TODO

- **回測與效能評估**：可加入歷史資料回放機制，驗證多代理人策略穩定性，衡量 Sharpe Ratio、MDD 等。
- **實盤**：整合真實券商 API (如 Interactive Brokers, Alpaca) 進行小額實盤測試。
- **Prompt 優化**：微調 YAML 中的 Prompt，以降低 LLM 產生幻覺或雜訊輸出的機率。 (搭配回測)
- **更多分析師**：未來可增加 ESG 風險分析、併購消息監控等，擴充研究維度。


