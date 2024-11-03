from celery import Celery
import os
from decouple import config
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_project.settings')

app=Celery('django_project')

app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks()
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")