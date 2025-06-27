import streamlit as st
import os
import importlib.util
import inspect

# User Mode Control
modes = {
    "Beginner": {
        "show_groups": ["Overview", "Bots", "Auto", "User Guide", "Maintenance", "Help"],
        "tips": True, "fire_and_forget": True
    },
    "Intermediate": {
        "show_groups": ["Overview", "Bots", "Analytics", "User Guide", "Alerts", "Maintenance", "Help"],
        "tips": True, "fire_and_forget": False
    },
    "Pro": {
        "show_groups": [
            "Overview", "Bots", "Analytics", "ML", "Market Intelligence", "Alerts",
            "Config", "Maintenance", "User Guide", "Overlay", "Integration Hubs", "Help"
        ],
        "tips": False, "fire_and_forget": False
    },
    "Enterprise": {
        "show_groups": ["All"],
        "tips": False, "fire_and_forget": False, "pro_features": True
    }
}
selected_mode = st.sidebar.selectbox(
    "User Mode",
    list(modes.keys()),
    index=0 if "app_mode" not in st.session_state else list(modes.keys()).index(st.session_state["app_mode"])
)
st.session_state["app_mode"] = selected_mode
active_mode = modes[selected_mode]

# --- Auto-discover all *_panel.py files and integrations ---
def discover_panels(directory):
    panels = {}
    for fname in os.listdir(directory):
        if fname.endswith("_panel.py") and fname != "master_dashboard.py":
            modulename = fname[:-3]
            path = os.path.join(directory, fname)
            spec = importlib.util.spec_from_file_location(modulename, path)
            mod = importlib.util.module_from_spec(spec)
            try:
                spec.loader.exec_module(mod)
                for name, func in inspect.getmembers(mod, inspect.isfunction):
                    if name.endswith("_panel") and not name.startswith("_"):
                        panels[name] = func
            except Exception as e:
                st.warning(f"Failed to import {fname}: {e}")
    # Subdir integrations (for integration_panels/)
    integrations_path = os.path.join(directory, "integration_panels")
    if os.path.exists(integrations_path):
        for fname in os.listdir(integrations_path):
            if fname.endswith("_panel.py"):
                modulename = f"integration_panels.{fname[:-3]}"
                path = os.path.join(integrations_path, fname)
                spec = importlib.util.spec_from_file_location(modulename, path)
                mod = importlib.util.module_from_spec(spec)
                try:
                    spec.loader.exec_module(mod)
                    for name, func in inspect.getmembers(mod, inspect.isfunction):
                        if name.endswith("_panel") and not name.startswith("_"):
                            panels[name] = func
                except Exception as e:
                    st.warning(f"Failed to import {fname}: {e}")
    return panels

panels_dir = os.path.dirname(os.path.abspath(__file__))
all_panels = discover_panels(panels_dir)

# --- Registry: group panels by function/type (update as you add more) ---
panel_registry = {
    "Overview": [
        "onboarding_panel", "executive_dashboard_panel"
    ],
    "Bots": [
        "bots_overview_panel", "bot_control_panel", "trade_journal_panel"
    ],
    "Auto": [
        "auto_mode_panel"
    ],
    "Analytics": [
        "analytics_panel", "performance_visualizer_panel", "risk_dashboard_panel"
    ],
    "ML": [
        "ml_analytics_panel"
    ],
    "Market Intelligence": [
        "market_intelligence_panel", "tradingview_widget_panel"
    ],
    "Alerts": [
        "alert_manager_panel", "llm_audit_panel"
    ],
    "Config": [
        "config_hot_reload_panel", "maintenance_panel"
    ],
    "Maintenance": [
        "maintenance_panel"
    ],
    "User Guide": [
        "user_guide_panel"
    ],
    "Overlay": [
        "overlay_manager_panel", "monitoring_overlay"
    ],
    "Integration Hubs": [
        "coinglass_panel", "coingecko_panel", "coinstats_panel", "banterbubbles_panel"
    ],
    "Help": [
        "guided_tour_panel", "command_palette_panel"
    ],
}

def group_tabs_for_mode():
    groups = active_mode["show_groups"]
    if "All" in groups:
        groups = list(panel_registry.keys())
    tab_groups = []
    tab_funcs = []
    for group in groups:
        if group in panel_registry:
            for panel in panel_registry[group]:
                if panel in all_panels:
                    tab_groups.append(f"{group}: {panel.replace('_panel','').replace('_',' ').title()}")
                    tab_funcs.append(all_panels[panel])
    return tab_groups, tab_funcs

tab_names, tab_funcs = group_tabs_for_mode()
selected_tab = st.sidebar.radio("App Sections", tab_names, index=0)
panel_func = tab_funcs[tab_names.index(selected_tab)]
panel_func()  # Render selected panel

st.sidebar.markdown("---")
if active_mode.get("tips", False):
    st.sidebar.info("Beginner mode is ON. Extra tips and explanations will be shown.")
st.sidebar.caption("OmegaSignalPro v3.0 © 2025 All Rights Reserved")