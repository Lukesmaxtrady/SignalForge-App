import streamlit as st
import pandas as pd
import os

def analytics_panel():
    st.header("📊 Analytics Dashboard")
    st.write("See live PnL, Sharpe, drawdown, and performance analytics.")
    path = "data/reports/performance.csv"
    if os.path.exists(path):
        df = pd.read_csv(path)
        st.line_chart(df.set_index("date")["equity"])
        st.area_chart(df.set_index("date")[["sharpe", "drawdown"]])
        st.write(df.tail(10))
    else:
        st.info("Performance analytics not available yet.")