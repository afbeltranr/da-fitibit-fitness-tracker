# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install GitHub Copilot
RUN curl -fsSL https://deb.nodesource.com/setup_14.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g @githubnext/github-copilot-cli \
    && github-copilot-cli auth

# Install Jupyter and other Python dependencies
RUN pip install --no-cache-dir \
    jupyter \
    notebook \
    ipykernel \
    pandas \
    numpy \
    matplotlib \
    seaborn \
    scikit-learn

# Set up a working directory
WORKDIR /workspace

# Expose Jupyter Notebook port
EXPOSE 8888

# Start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]