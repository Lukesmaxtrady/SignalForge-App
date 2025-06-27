import streamlit as st
import os
import requests
import pandas as pd

def send_discord_alert(msg):
    webhook = os.getenv("DISCORD_WEBHOOK_URL")
    if webhook:
        requests.post(webhook, json={"content": msg})

def send_telegram_alert(msg):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if token and chat_id:
        requests.get(
            f"https://api.telegram.org/bot{token}/sendMessage",
            params={"chat_id": chat_id, "text": msg}
        )

def alert_manager_panel():
    st.header("🚨 Alert Manager & Real-Time Streaming")
    st.write("Configure real-time alerts for trades, anomalies, system errors, and regime changes. See live alert logs and simulate sending an alert below.")
    
    enable_telegram = st.toggle("Enable Telegram Alerts", value=os.getenv("TELEGRAM_ALERTS", "1") == "1")
    enable_discord = st.toggle("Enable Discord Alerts", value=os.getenv("DISCORD_ALERTS", "0") == "1")
    enable_slack = st.toggle("Enable Slack Alerts", value=os.getenv("SLACK_ALERTS", "0") == "1")
    enable_email = st.toggle("Enable Email Alerts (premium)", value=os.getenv("EMAIL_ALERTS", "0") == "1")
    enable_cloud_premium = st.toggle("Enable Advanced Cloud Alerting (Paid)", value=False)

    st.caption("Premium and cloud alerts may require additional setup and may incur extra fees. Alerts will be sent for all critical trading events, risk, and system events.")
    
    # Simulate sending an alert
    st.subheader("Send Test Alert")
    test_msg = st.text_input("Test Alert Message", value="🚨 Test alert: Example alert from OmegaSignalPro.")
    if st.button("Send Test Alert"):
        if enable_discord:
            send_discord_alert(test_msg)
        if enable_telegram:
            send_telegram_alert(test_msg)
        st.success("Test alert sent (check your configured channels).")
    
    # Show last 10 alerts (log file)
    st.subheader("Recent Alerts")
    log_file = "data/reports/alerts.log"
    if os.path.exists(log_file):
        df = pd.read_csv(log_file, names=["timestamp", "message"])
        st.dataframe(df.tail(10), use_container_width=True)
    else:
        st.info("No alerts sent yet.")
    
    if enable_cloud_premium:
        st.success("Advanced cloud alerting enabled (requires cloud setup). Configure via the Maintenance panel.")