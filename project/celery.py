import os
import time

from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')
app.config_from_object(settings , namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


@app.task(bind=True)
def add(self, x, y):
    time.sleep(7)
    print(f"{x} + {y} = {x+y}")
    return x + y


@app.task(bind=True)
def mul(self, x, y):
    time.sleep(3)
    print(f"{x} * {y} = {x*y}")
    return x * y







