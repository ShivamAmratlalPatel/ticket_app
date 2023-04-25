# Base image
FROM python:3.11-slim-buster

# Set working directory
WORKDIR /app

# Copy the poetry.lock file and pyproject.toml file
COPY poetry.lock pyproject.toml ./

# Install dependencies
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-dev

# Copy the application code
COPY . .

# Expose port 8000
EXPOSE 8000

# Run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
