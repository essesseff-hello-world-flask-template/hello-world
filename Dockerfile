# Use official Python runtime as base image
FROM python:3.14-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies (--system avoids creating a venv inside the container)
RUN uv pip install --system --no-cache -r requirements.txt

# Copy application files
COPY . .

# Expose port 8080
EXPOSE 8080

# Set environment variables
ENV PORT=8080

# Run the application with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "--timeout", "60", "app:app"]
