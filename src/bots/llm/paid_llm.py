from openai import OpenAI

class PaidLLMBot:
    def __init__(self, provider="openai", api_key=None, model="gpt-4o"):
        self.provider = provider
        self.api_key = api_key
        self.model = model
        if provider == "openai":
            self.client = OpenAI(api_key=api_key)
        # Extend for Claude, Gemini, etc.

    def ask(self, prompt):
        if self.provider == "openai":
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=512,
            )
            return response.choices[0].message.content
        else:
            raise NotImplementedError("Provider not yet implemented.")

    def status(self):
        return {"bot": "PaidLLM", "status": "ready"}
