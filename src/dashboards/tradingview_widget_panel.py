import streamlit as st

def tradingview_widget_panel():
    st.header("📈 TradingView Live Chart Widget")
    st.write("Embedded TradingView chart for live market action.")
    symbol = st.text_input("Symbol", value="BINANCE:BTCUSDT")
    interval = st.selectbox("Interval", ["1", "5", "15", "60", "240", "D"], index=3)
    st.markdown(f"""
<iframe src="https://www.tradingview.com/widgetembed/?frameElementId=tradingview_c4e09&symbol={symbol}&interval={interval}&hidesidetoolbar=1&hidetoptoolbar=1" width="100%" height="480" frameborder="0"></iframe>
""", unsafe_allow_html=True)