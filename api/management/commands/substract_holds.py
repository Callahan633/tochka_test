import schedule
import time

from django.core.management.base import BaseCommand

from api.cronjob import run_threaded, scheduled_task


class Command(BaseCommand):
    def handle(self, *args, **options):
        schedule.every(10).seconds.do(run_threaded, scheduled_task)
        while True:
            schedule.run_pending()
            time.sleep(1)
