# Use Python 3.11 as the base image
FROM python:3.11-slim-buster

# Install awscli
RUN apt update -y && apt install awscli -y

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Upgrade accelerate separately
RUN pip install --upgrade accelerate

# Uninstall transformers and accelerate, then reinstall them
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate


# Define the command to run the app
CMD ["python3", "app.py"]
