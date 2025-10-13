#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Change to the script's directory to ensure all paths are relative to the project root.
cd "$(dirname "$0")"

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install the required packages using pip
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Run the Streamlit application
echo "Launching the VA Insights Engine..."
streamlit run app.py
