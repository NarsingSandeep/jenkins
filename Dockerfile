# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script to the container's working directory
COPY python.py /app/

# Install any dependencies (optional, if your Python script requires them)
# RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script
CMD ["python", "python.py"]
