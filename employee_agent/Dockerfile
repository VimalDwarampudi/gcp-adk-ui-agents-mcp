# Use a slim Python 3.12 image to keep it lightweight
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY Leave_Policy.pdf /app/Leave_Policy.pdf
# Copy the rest of your application code
COPY . .

# Expose the port your FastAPI app runs on
EXPOSE 8000

# Run the application
# Note: Using 0.0.0.0 is required for Docker to allow external access
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]