import streamlit as st
import pandas as pd

def bots_overview_panel():
    st.header("🤖 Bots Overview")
    st.markdown("Status and performance of all bots (live, demo, prop).")
    # Example bots — in production, load dynamically from config/logs
    bots = [
        {"name": "MainTrader", "mode": "Live", "exchange": "Bitget", "pnl": 3200, "drawdown": -2.1, "win_rate": 0.68, "prop_firm": "None"},
        {"name": "ArbBot", "mode": "Demo", "exchange": "Blofin", "pnl": 450, "drawdown": -0.8, "win_rate": 0.62, "prop_firm": "None"},
        {"name": "AlphaCap-Prop", "mode": "Prop", "exchange": "Bitget", "pnl": 21000, "drawdown": -5.0, "win_rate": 0.72, "prop_firm": "Alpha Capital"},
    ]
    df = pd.DataFrame(bots)
    st.dataframe(df, use_container_width=True)
    selected_bot = st.selectbox("Select bot for detail/control:", df["name"])
    if selected_bot:
        bot = df[df["name"] == selected_bot].iloc[0]
        st.subheader(f"{bot['name']} ({bot['mode']})")
        st.markdown(f"- **Exchange:** {bot['exchange']}")
        st.markdown(f"- **PnL:** ${bot['pnl']}")
        st.markdown(f"- **Drawdown:** {bot['drawdown']}%")
        st.markdown(f"- **Win Rate:** {100*bot['win_rate']:.1f}%")
        st.button("Start")
        st.button("Pause")
        st.button("Stop")
        st.info("See other panels for advanced analytics and tuning.")