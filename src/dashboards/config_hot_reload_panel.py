import streamlit as st
import yaml
import os

def config_hot_reload_panel():
    st.header("⚙️ Live Config Editor & Hot-Reload")
    st.write("Edit any YAML config, save, and hot-reload. All modules will pick up new configs on next tick—no restart needed!")
    
    configs = {
        "Bot Config": "config/config.yaml",
        "Dashboard": "config/dashboard.yaml",
        "Exchanges": "config/exchanges.yaml",
        "Prop Firms": "config/prop_firms.yaml"
    }
    selected = st.selectbox("Select Config", list(configs.keys()))
    config_path = configs[selected]
    
    # Load file contents
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            yaml_text = f.read()
    else:
        yaml_text = ""
    yaml_edit = st.text_area("Edit YAML", yaml_text, height=350)
    
    # Save and reload
    if st.button("Save and Reload"):
        with open(config_path, "w") as f:
            f.write(yaml_edit)
        st.success(f"{selected} saved! All modules will reload config on next trade/job.")