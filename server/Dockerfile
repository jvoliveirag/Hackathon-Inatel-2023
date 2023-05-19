# Use an official Python runtime as the base image
FROM python:3.9-slim

RUN apt-get update && \
      apt-get -y install sudo

# Set the working directory in the container
WORKDIR .

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app directory into the container
COPY . .

# Set the command to run the App
CMD ["sudo", "python", "traffic_analyzer.py"]
