# Use the official Python image from Docker Hub
FROM python:3.10.11

# Set the working directory inside the container
WORKDIR /app

# Copy the local directory contents into the container
COPY . /app

# Install system dependencies, including libpq-dev
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

    
# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files (ensure that `STATIC_ROOT` is set correctly in settings.py)
RUN python manage.py collectstatic --noinput


# Expose the port your app runs on
EXPOSE 8000

# Command to run the Django development server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "puddle.wsgi:application"]
