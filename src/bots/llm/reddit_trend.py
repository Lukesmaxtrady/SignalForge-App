import requests

class RedditTrendBot:
    def __init__(self, subreddits, sentiment_analyzer):
        self.subreddits = subreddits
        self.sentiment = sentiment_analyzer

    def fetch_trends(self):
        posts = []
        for sub in self.subreddits:
            url = f"https://www.reddit.com/r/{sub}/hot.json?limit=20"
            headers = {"User-Agent": "SignalForgeBot"}
            try:
                resp = requests.get(url, headers=headers, timeout=5)
                resp.raise_for_status()
                data = resp.json()
                posts.extend(data.get("data", {}).get("children", []))
            except Exception:
                continue
        return posts

    def get_sentiment_trends(self):
        posts = self.fetch_trends()
        summaries = []
        for post in posts:
            title = post.get("data", {}).get("title", "")
            sentiment = self.sentiment.analyze(title)
            summaries.append({"title": title, "sentiment": sentiment})
        return summaries

    def status(self):
        return {"bot": "RedditTrendBot", "status": "ready"}
