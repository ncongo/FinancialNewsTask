from __future__ import absolute_import
import os
from celery import Celery

from celery.schedules import crontab # scheduler

# default django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FinancialNews.settings')

app = Celery('FinancialNews')

app.conf.timezone = 'UTC'

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'scraping.tasks.financialnews_rss',
        'schedule': 30.0
    },
}

app.autodiscover_tasks()