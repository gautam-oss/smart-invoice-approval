FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    gcc \
    python3-dev \
    musl-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Create media directory
RUN mkdir -p /app/media/invoices

# Collect static files (will run in docker-compose command)
# RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Default command (overridden in docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]