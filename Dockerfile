# Use the official Python base image with Bullseye variant
FROM python:3.11-bullseye

# Install GDAL, PostgreSQL client, and other necessary packages for GeoDjango
RUN apt-get update && \
    apt-get install -y binutils libproj-dev gdal-bin postgresql-client libpq-dev

# Set the working directory
WORKDIR /app

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port on which the app will run
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
