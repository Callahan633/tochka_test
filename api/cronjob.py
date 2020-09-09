import threading

from api.models import Account


def scheduled_task():
    for item in Account.objects.all():
        if item.is_opened:
            if item.current_balance - item.reserved_operations >= 0:
                item.current_balance -= item.reserved_operations
                item.reserved_operations = 0
                item.save()


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

