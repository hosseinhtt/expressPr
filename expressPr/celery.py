import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'expressPr.settings')
app = Celery('expressPr')
app.config_from_object('django.conf:settings', namespace='CELERY')
