import os
import requests

def send_discord_alert(msg):
    webhook = os.getenv("DISCORD_WEBHOOK_URL")
    if webhook:
        try:
            requests.post(webhook, json={"content": msg})
        except Exception as e:
            print("Discord alert error:", e)

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

def send_slack_alert(msg):
    webhook = os.getenv("SLACK_WEBHOOK_URL")
    if webhook:
        try:
            requests.post(webhook, json={"text": msg})
        except Exception as e:
            print("Slack alert error:", e)

def send_alerts(msg, to=("discord", "telegram", "slack")):
    if "discord" in to:
        send_discord_alert(msg)
    if "telegram" in to:
        send_telegram_alert(msg)
    if "slack" in to:
        send_slack_alert(msg)