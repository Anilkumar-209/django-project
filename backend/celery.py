"""
celery configuration for the django backend project.

- sets default django settings module
- creates celery app named 'backend'
- loads settings with 'celery_' namespace
- auto-discovers tasks from installed apps
"""

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
app = Celery('backend')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
