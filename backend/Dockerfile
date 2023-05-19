# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Updating linux package lists
RUN apt-get update && apt-get install -y --no-install-recommends tk-dev && rm -r /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app directory into the container
COPY /app .

# Set the environment variable for Flask
ENV UI_INJECTION="Flask"

# Set the command to run the App
CMD ["python", "-m" "src.main"]
