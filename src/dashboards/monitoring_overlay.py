import streamlit as st
import os

def monitoring_overlay():
    st.markdown("""
    <style>
    .monitor-bar {
        background: #181C23;
        color: #10A3F7;
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 12px;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)
    # Simulate live health (replace with actual status checks)
    st.markdown("""
    <div class="monitor-bar">
    ✅ Bot Health: <b>Healthy</b> &nbsp; | &nbsp;
    🟢 Data: <b>Fresh</b> &nbsp; | &nbsp;
    🟢 API: <b>Connected</b> &nbsp; | &nbsp;
    🟢 Alerts: <b>None</b>
    </div>
    """, unsafe_allow_html=True)