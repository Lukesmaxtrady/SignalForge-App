import os
import requests

def send_telegram_alert(msg):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if token and chat_id:
        try:
            requests.get(
                f"https://api.telegram.org/bot{token}/sendMessage",
                params={"chat_id": chat_id, "text": msg}
            )
        except Exception as e:
            print("Telegram alert error:", e)