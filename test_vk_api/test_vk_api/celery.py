from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_vk_api.settings')

app = Celery('test_vk_api')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'service.tasks.task_get_',
#         'schedule': 30.0,
#     },
# }

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

