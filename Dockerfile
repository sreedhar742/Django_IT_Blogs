FROM python:3.10-slim


WORKDIR /app

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev build-essential default-mysql-client \
    && apt-get clean
COPY . /app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "django_project.wsgi:application"]
