# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y unzip
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Set Kaggle credentials as environment variables
ENV KAGGLE_USERNAME=${KAGGLE_USERNAME}
ENV KAGGLE_KEY=${KAGGLE_KEY}

# Download and unzip the dataset
RUN kaggle datasets download -d arashnic/fitbit -p data/ && \
    unzip -o data/*.zip -d data/ && \
    rm data/*.zip

# Command to run the application
CMD ["python", "scripts/main.py"]