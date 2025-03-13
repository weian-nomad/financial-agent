# agent_base.py
import yaml
import re
import json
import ollama

class BaseLLMAgent:
    def __init__(self, config_path: str):
        with open(config_path, 'r', encoding='utf-8') as file:
            self.config = yaml.safe_load(file)
        self.prompt_template = self.config['prompt_template']
        self.model_name = self.config.get('model_name', 'deepseek-r1:70b')
        self.max_retries = self.config.get('max_retries', 3)

    def generate_with_llm(self, prompt: str) -> str:
        """
        呼叫 ollama.generate() 並串接回應
        """
        final_output = []
        for chunk in ollama.generate(model=self.model_name, prompt=prompt):
            key, val = chunk
            if key == "response":
                final_output.append(val)
        return "".join(final_output)

    def parse_response(self, raw_text: str, default_structure=None) -> dict:
        if default_structure is None:
            default_structure = {}

        # 移除 ```json 或 ``` 之類的 code fence
        cleaned_text = re.sub(r'```json|```', '', raw_text, flags=re.IGNORECASE)
        # 用正則尋找第一個 { ... } 區塊
        match = re.search(r'(\{.*\})', cleaned_text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1))
            except:
                return default_structure
        return default_structure

    def run(self, **kwargs) -> dict:
        """
        主流程：代入參數到 Prompt，呼叫 LLM，多次重試 & 解析
        """
        prompt = self.prompt_template.format(**kwargs)
        for attempt in range(self.max_retries):
            raw_response = self.generate_with_llm(prompt)
            result = self.parse_response(raw_response, default_structure={})
            if result:  # 若成功解析到 JSON
                return result
        return {}  # 若最終仍失敗，回傳空字典
