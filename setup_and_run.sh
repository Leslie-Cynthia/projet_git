#!/bin/bash

echo "🔧 Setting up virtual environment..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install dash pandas plotly gunicorn

echo "🚀 Launching the Dash server with Gunicorn..."
venv/bin/gunicorn app:server --bind 0.0.0.0:8050 --daemon

echo "✅ Server running at http://localhost:8050 or http://<your-ip>:8050"
