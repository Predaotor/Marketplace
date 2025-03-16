FROM python:3.10.11

EXPOSE 8080

# Prevent Python from writing .pyc files and set unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    build-essential \
    postgresql-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install pip requirements
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Create a non-root user and set permissions
RUN adduser --disabled-password --gecos "" appuser

# Set working directory
WORKDIR /app

# Copy app files and fix permissions
COPY . /app
RUN chown -R appuser:appuser /app

# Copy and set permissions for entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Switch to non-root user
USER appuser

# Use entrypoint script to manage startup
ENTRYPOINT ["/entrypoint.sh"]
