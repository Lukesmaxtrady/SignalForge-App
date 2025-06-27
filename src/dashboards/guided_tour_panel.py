import streamlit as st

def guided_tour_panel():
    st.header("🗺️ Guided Tour")
    st.markdown("""
Welcome to OmegaSignalPro!  
- Use the sidebar to explore: Onboarding, Bots, Analytics, Market Intelligence, and more.
- Each panel has tooltips and pro tips in Beginner/Intermediate mode.
- Use the User Guide for step-by-step best practices.
- See Monitoring Overlay at the top for instant app health!
""")
    if st.button("Next: Go to Onboarding"):
        st.session_state["App Sections"] = "Overview: Onboarding Panel"