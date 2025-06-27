import requests

class NewsNarrativeBot:
    def __init__(self, api_endpoint, sentiment_analyzer):
        self.api_endpoint = api_endpoint
        self.sentiment = sentiment_analyzer

    def fetch_news(self, keyword):
        resp = requests.get(f"{self.api_endpoint}/news?query={keyword}")
        return resp.json().get("articles", [])

    def analyze_narratives(self, keyword):
        articles = self.fetch_news(keyword)
        result = []
        for article in articles:
            content = article.get("content", "")
            sentiment = self.sentiment.analyze(content)
            result.append({"headline": article.get("title", ""), "sentiment": sentiment})
        return result

    def status(self):
        return {"bot": "NewsNarrative", "status": "ready"}
