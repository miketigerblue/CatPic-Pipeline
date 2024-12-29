# Use a lightweight Python base image
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Expose port 5000
EXPOSE 5001

# Run the Flask app
CMD ["python", "app.py"]
