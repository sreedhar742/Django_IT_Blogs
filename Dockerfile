
FROM python:3.10-slim


WORKDIR /app


COPY . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=django_project.settings


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "django_project.wsgi:application"]
