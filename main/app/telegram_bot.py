import requests
from .config import TELEGRAM_TOKEN

class TelegramBot:
    def __init__(self):
        self.base_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

    def send_message(self, chat_id, text):
        url = f"{self.base_url}/sendMessage"
        data = {"chat_id": chat_id, "text": text}
        try:
            resp = requests.post(url, data=data, timeout=10)
            resp.raise_for_status()
            return True
        except Exception as e:
            print(f"Telegram error: {e}")
            return False
