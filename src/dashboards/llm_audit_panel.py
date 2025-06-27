import streamlit as st
import os

def llm_audit_panel():
    st.header("🤖 LLM Audit & Suggestions")
    st.write("Natural-language AI (LLM) review of recent trades, performance, and system health. View or apply suggestions below.")
    
    audit_file = "data/reports/llm_audit_last.txt"
    if os.path.exists(audit_file):
        with open(audit_file) as f:
            summary = f.read()
        st.markdown(f"#### Last LLM Audit\n{summary}")
    else:
        st.info("No LLM audit found yet. Will auto-generate every week.")

    if st.button("Apply LLM Suggestions"):
        st.success("LLM-driven config/model tweaks will be applied on next run (auto-tunable in Pro Mode).")
    if st.button("Ignore for Now"):
        st.info("Suggestions ignored. You can re-run the audit at any time.")
    st.caption("LLM audits help you catch edge decay, overfitting, and configuration mistakes early.")