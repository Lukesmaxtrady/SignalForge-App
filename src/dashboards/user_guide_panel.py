import streamlit as st

def user_guide_panel():
    st.header("📘 User Guide & Best Practices")
    st.markdown("""
### Capital Preservation & Profit Maximization

- **Start in Demo/Shadow Mode:** Run bots on paper for 4+ weeks before risking real funds.
- **Enable All Risk Controls:** Never disable daily loss, max drawdown, or stop-loss features—even in demo.
- **Backtest and Stress-Test:** Use the app’s backtest and scenario tools on multiple symbols and timeframes before deploying live.
- **Diversify Strategies:** Don’t rely on just one edge; combine momentum, mean reversion, ML/meta-label, and regime switching.
- **Monitor Edge Decay:** Regularly check rolling Sharpe, win rate, and live model audit overlays—rotate out underperformers.
- **Use Shadow/Live Toggle:** Always keep a “shadow” version of your bot running in parallel for real-time validation.
- **Never Trust Free Data for Live Trading:** For real capital, use premium feeds (Polygon, Intrinio, etc.); toggle in-app.
- **Enable Pro Alerts:** Get instant notifications on any risk or system breach (Telegram, Discord, Slack, Email).

---

### Ongoing Perfection & App Operation

- **Set Your Mode:** Choose Beginner/Intermediate/Pro/Enterprise—start simple, then unlock advanced tools as you learn.
- **Review the Executive Dashboard:** All your KPIs and alerts in one glance. Use “Quick Actions” for instant control.
- **Automate Maintenance:** Let the Maintenance panel handle backups, log cleanup, and API/data checks.
- **Apply AI Audit Suggestions:** Review weekly LLM audit recommendations, apply safe config/model tweaks with one click.
- **Check the Command Palette:** Press `/` to quickly jump to bots, logs, configs, actions, or help.
- **If Unsure, Pause:** Use the sidebar “Pause All Bots” if anything feels off. Use logs and audit trails to review.
- **Encourage Feedback:** Use the in-app feedback button for suggestions or issues.

---

### Key “Do’s” for Capital Preservation

- **Always trade with risk controls ON.**
- **Limit capital exposure per bot and symbol.**
- **If a model or bot’s performance degrades, rotate it out and shadow it before going live again.**
- **Keep up with maintenance alerts—don’t ignore API expiry or data drift warnings.**
- **Preserve your audit logs and backups—use the Maintenance panel to export regularly.**

---

### Maximizing Profits

- **Leverage the performance visualizer to spot “hot” strategies or symbols.**
- **Use auto-retrain and LLM audit to keep models fresh.**
- **Diversify across exchanges, prop firms, and strategies.**
- **Continuously monitor, learn, and adapt—never “set and forget” for long!**

---
""")
    st.success("Your capital is precious. This app is built to help you preserve and grow it like a professional.")
    st.caption("For full documentation and tips, visit [OmegaSignalPro Docs](https://github.com/Lukesmaxtrady/OmegaSignalPro-v3.0/wiki)")