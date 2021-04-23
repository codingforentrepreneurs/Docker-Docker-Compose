import time
from celery import shared_task

@shared_task
def hello_world(num=10):
    time.sleep(num)
    print(f"Hello world {num}")