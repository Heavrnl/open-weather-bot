# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
#EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Rename .env.dist to .env
RUN mv .env.dist .env

# Run bot.py when the container launches
CMD ["python", "bot.py"]
