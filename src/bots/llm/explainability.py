from openai import OpenAI

class ExplainabilityBot:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def explain_signal(self, signal_dict):
        prompt = (
            "Explain this trading signal and its reasoning in plain English: "
            + str(signal_dict)
        )
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=256,
        )
        return response.choices[0].message.content

    def status(self):
        return {"bot": "Explainability", "status": "ready"}
