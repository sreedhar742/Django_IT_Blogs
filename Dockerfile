FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install MySQL development libraries and mysql-client
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev build-essential default-mysql-client \
    && apt-get clean

# Copy the application code into the container
COPY . /app

# Upgrade pip
RUN pip install --upgrade pip

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "django_project.wsgi:application"]
