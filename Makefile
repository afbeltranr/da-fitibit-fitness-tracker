# Variables
DATA_DIR = data/
VENV = .venv

# Default command
.PHONY: all
all: install_env download_data run_script cleanup

# 1. Set up virtual environment and install dependencies
install_env:
    python3 -m venv $(VENV)
    . $(VENV)/bin/activate && pip install -r requirements.txt

# 2. Download the dataset using Kaggle API and unzip it
download_data:
    . $(VENV)/bin/activate && kaggle datasets download -d arashnic/fitbit -p $(DATA_DIR)
    unzip -o $(DATA_DIR)/*.zip -d $(DATA_DIR)
    rm $(DATA_DIR)/*.zip

# 3. Run the Python script
run_script:
    . $(VENV)/bin/activate && python scripts/main.py

# 4. Cleanup virtual environment
cleanup:
    rm -rf $(VENV)