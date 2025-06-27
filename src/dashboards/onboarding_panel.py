import streamlit as st

def onboarding_panel():
    st.header("👋 Welcome to OmegaSignalPro!")
    st.markdown("""
- Automated AI/ML trading signals, dashboards, analytics, and capital protection.
- Connect your exchanges, set your risk, and let the bot handle the rest!
- Use the sidebar to explore all features, or start the guided tour.
""")
    st.subheader("Quick Start Steps:")
    st.markdown("""
1. Set your API keys in the Integrations panel.
2. Upload/fetch historical data in the Data Fetcher.
3. Tune your strategies in AI Model Tuning.
4. Start demo trading or go live!
""")
    st.info("Use Beginner Mode to show extra help and safety tips. Switch to Pro mode for all advanced controls!")