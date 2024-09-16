# Variables
DATA_DIR = data/
VENV = .venv

# Default command
.PHONY: all
all: install_env download_data run_script cleanup

# 1. Set up Poetry environment and install dependencies
install_env:
    poetry install

# 2. Download the dataset using Kaggle API
download_data:
    poetry run kaggle datasets download -d arashnic/fitbit --unzip -p $(DATA_DIR)

# 3. Run the Python script
run_script:
    poetry run python scripts/main.py