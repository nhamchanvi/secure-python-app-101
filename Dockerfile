# Dockerfile

# 1. Use an official Python runtime as a parent image
FROM python:3.11-slim AS builder

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set the working directory in the container
WORKDIR /app

# 4. Install dependencies
# Copy only requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the application code into the container
COPY . .

# 6. Define the command to run the application using Gunicorn
# Expose the port the app runs on
EXPOSE 5000

# Run the application using Gunicorn
# Use 0.0.0.0 to be accessible from outside the container
# The number of workers can be adjusted based on expected load/CPU cores
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]