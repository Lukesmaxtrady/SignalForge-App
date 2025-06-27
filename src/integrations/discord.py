import os
import requests

def send_discord_alert(msg):
    webhook = os.getenv("DISCORD_WEBHOOK_URL")
    if webhook:
        try:
            requests.post(webhook, json={"content": msg})
        except Exception as e:
            print("Discord alert error:", e)