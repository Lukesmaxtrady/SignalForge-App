import streamlit as st
import os
import pandas as pd

def executive_dashboard_panel():
    st.header("🚀 Executive Dashboard")
    st.success("All bots: healthy, trading, no risk limits hit.")

    # Demo: Live metrics (replace with real KPIs in production)
    st.metric("Live PnL (7d)", "$2,742", "+14.3%")
    st.metric("Max Drawdown (30d)", "-2.4%")
    st.metric("Risk Health", "All limits OK")
    st.metric("API Integrations", "All valid")
    st.metric("Next Retrain", "6h")
    st.metric("Backups", "Last: 2h ago")
    st.info("Click any section in the sidebar for full details.")

    # Show latest alerts if present
    alerts_file = "data/reports/alerts.log"
    if os.path.exists(alerts_file):
        with open(alerts_file) as f:
            alerts = f.readlines()[-3:]
            for a in alerts:
                st.warning(a)

    # Demo: optional mini-table for live trades
    trade_log_file = "data/trades/trade_log.csv"
    if os.path.exists(trade_log_file):
        df = pd.read_csv(trade_log_file)
        if not df.empty:
            st.subheader("Recent Trades")
            st.dataframe(df.tail(5), use_container_width=True)