from django.core.management.base import BaseCommand

from api.models import Account


class Command(BaseCommand):
    def handle(self, *args, **options):
        for item in Account.objects.all():
            if item.is_opened:
                if item.current_balance - item.reserved_operations >= 0:
                    item.current_balance -= item.reserved_operations
                    item.reserved_operations = 0
                    item.save()
