#!/bin/bash
echo "Deploying SignalForge to Render.com..."
git add .
git commit -m "Deploy: $(date +'%Y-%m-%d %H:%M')"
git push render main
echo "Deployment initiated! Check Render dashboard for status."
