import requests

class Notifier:
    def __init__(self, telegram_token=None, discord_webhook=None, voice_enabled=False):
        self.telegram_token = telegram_token
        self.discord_webhook = discord_webhook
        self.voice_enabled = voice_enabled

    def send_telegram(self, chat_id, message):
        if self.telegram_token:
            url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
            requests.post(url, data={"chat_id": chat_id, "text": message})

    def send_discord(self, message):
        if self.discord_webhook:
            requests.post(self.discord_webhook, json={"content": message})

    def play_voice(self, phrase):
        if self.voice_enabled:
            # Placeholder: integrate with voice_alerts service
            print(f"[VOICE] {phrase}")

    def notify_all(self, message, chat_id=None):
        self.send_telegram(chat_id, message)
        self.send_discord(message)
        self.play_voice(message)
