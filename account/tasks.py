from celery import shared_task
import time

@shared_task
def print_wellcome(n):
    time.sleep(n)
    print('Wellcome to Django')