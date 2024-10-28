# FROM python:3.10-slim

# # Set the working directory
# WORKDIR /app

# # Copy the requirements file and install dependencies
# COPY requirements.txt .
# RUN apt-get update && apt-get install -y \
#     default-libmysqlclient-dev \
#     build-essential \
#     default-mysql-client && \
#     apt-get clean

# RUN pip install --upgrade pip
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the project files
# COPY . .

# # Copy the .env file
# COPY .env .

# # Collect static files
# RUN python manage.py collectstatic --noinput

# # Expose the port
# EXPOSE 8000

# # Command to run the application
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "django_project.wsgi:application"]
# Use the official Python 3.10-slim image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    default-mysql-client && \
    apt-get clean

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the application port
EXPOSE 8000

# Command to apply migrations and start the application
CMD ["sh", "-c", "python manage.py migrate && gunicorn --bind 0.0.0.0:8000 --log-level debug django_project.wsgi:application"]
