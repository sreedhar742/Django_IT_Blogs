
: "${DJANGO_SETTINGS_MODULE:?Need to set DJANGO_SETTINGS_MODULE}"


python manage.py migrate


exec python manage.py runserver 0.0.0.0:8000
