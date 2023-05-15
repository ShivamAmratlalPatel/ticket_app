# Base image
FROM python:3.11-slim-buster

ENV PYTHONPATH=.

# Set working directory
WORKDIR /app/backend

# Copy the poetry.lock file and pyproject.toml file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose port 8000
EXPOSE 8000

# Run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]