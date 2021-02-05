import os
from datetime import timedelta

from celery import Celery

# set the default Django settings module for the 'celery' program.
import sys
sys.path.append('/home/wangdong/project/Admin/settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '/home/wangdong/project/Admin/settings/product_settings')
app = Celery('Admin')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(related_name='celery_tasks')
