#!/bin/bash
echo "Setting up SignalForge..."
python3 -m venv venv
source venv/bin/activate
pip install -r ../requirements.txt
cd ../frontend
npm install
cd ..
echo "Setup complete!"
