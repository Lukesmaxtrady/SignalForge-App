import streamlit as st
import pandas as pd
import os

def trade_journal_panel():
    st.header("📒 Trade Journal")
    st.write("Review historical and recent trades.")
    path = "data/trades/trade_log.csv"
    if os.path.exists(path):
        df = pd.read_csv(path)
        st.dataframe(df.tail(100), use_container_width=True)
    else:
        st.info("No trade logs yet.")
