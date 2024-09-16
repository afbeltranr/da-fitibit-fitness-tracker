# Variables
KAGGLE_USERNAME = afbeltranr
KAGGLE_KEY = 87c45fb942e43adcc6cb299842e99155
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
	export KAGGLE_USERNAME=$(KAGGLE_USERNAME) && export KAGGLE_KEY=$(KAGGLE_KEY)
	poetry run kaggle datasets download -d arashnic/fitbit --unzip -p $(DATA_DIR)

# 3. Run the Python script
run_script:
	poetry run python scripts/main.py

# 4. Clean up datasets
cleanup:
	rm -rf $(DATA_DIR)

# Additional utility commands:
.PHONY: visualize
visualize: run_script
	poetry run jupyter notebook

# Clean up everything (including virtual environment)
clean:
	rm -rf $(VENV) $(DATA_DIR)
