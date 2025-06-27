#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
echo "Setup complete! Edit your .env and run: streamlit run src/dashboards/master_dashboard.py"
