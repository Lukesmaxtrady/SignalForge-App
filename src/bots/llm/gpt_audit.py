from openai import OpenAI

class GPTAudit:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def audit_strategy(self, strategy_text):
        prompt = (
            "Audit the following trading strategy for risk, clarity, and edge. "
            "Return a summary and any detected flaws or improvements:\n\n"
            + strategy_text
        )
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=512,
        )
        return response.choices[0].message.content

    def status(self):
        return {"bot": "GPTAudit", "status": "ready"}
