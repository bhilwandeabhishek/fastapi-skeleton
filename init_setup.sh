# init_setup.sh

#!/usr/bin/env bash

set -e

echo "[$(date)]: START"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "[$(date)]: Creating virtual environment"
    python -m venv venv
fi

# Activate virtual environment
echo "[$(date)]: Activating virtual environment"

if [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
elif [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
else
    echo "ERROR: Virtual environment activation script not found."
    exit 1
fi

# Verify Python and pip point to the virtual environment
echo "Python: $(which python)"
python -m pip --version

# Install requirements
echo "[$(date)]: Installing requirements"
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
echo "[$(date)]: Running template.py"
python template.py

# Initialize Git if not already initialized
if [ ! -d ".git" ]; then
    echo "[$(date)]: Initializing Git repository"
    git init
else
    echo "[$(date)]: Git repository already initialized"
fi
echo "[$(date)]: Setup completed successfully"
