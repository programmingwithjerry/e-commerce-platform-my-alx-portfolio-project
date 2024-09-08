import os

from celery import Celery

# configure the default Django settings module for the 'celery' application.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myeshop.settings')

app = Celery('myeshop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
