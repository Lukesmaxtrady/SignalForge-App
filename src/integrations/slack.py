import os
import requests

def send_slack_alert(msg):
    webhook = os.getenv("SLACK_WEBHOOK_URL")
    if webhook:
        try:
            requests.post(webhook, json={"text": msg})
        except Exception as e:
            print("Slack alert error:", e)