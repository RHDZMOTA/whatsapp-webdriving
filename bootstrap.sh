#! /bin/bash

VENV_DIR="venv"
if [ ! -d "$VENV_DIR" ]; then
    virtualenv --python=python3 venv
fi

# Activate venv and install requirements
source venv/bin/activate
pip install -r requirements.txt

# create .env vars and run setup.
cp settings/.env.example settings/.env
python setup.py
