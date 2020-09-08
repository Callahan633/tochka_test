from django.core.management.base import BaseCommand

from api.models import Account


class Command(BaseCommand):
    def handle(self, *args, **options):
        mock_data = [
            {
                'credentials': 'Петров Иван Сергеевич',
                'current_balance': 1700,
                'reserved_operations': 300,
                'status': True
            },
            {
                'credentials': 'Kazitsky Jason',
                'current_balance': 200,
                'reserved_operations': 200,
                'status': True
            },
            {
                'credentials': 'Пархоменко Антон Александрович',
                'current_balance': 10,
                'reserved_operations': 300,
                'status': True
            },
            {
                'credentials': 'Петечкин Петр Измаилович',
                'current_balance': 1000000,
                'reserved_operations': 1,
                'status': False
            }
        ]
        for item in mock_data:
            Account.objects.create(
                credentials=item['credentials'],
                current_balance=item['current_balance'],
                reserved_operations=item['reserved_operations'],
                is_opened=item['status']
        )