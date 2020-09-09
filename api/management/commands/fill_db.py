from django.core.management.base import BaseCommand

from api.models import Account


class Command(BaseCommand):
    def handle(self, *args, **options):
        mock_data = [
            {
                'id': '26c940a1-7228-4ea2-a3bc-e6460b172040',
                'credentials': 'Петров Иван Сергеевич',
                'current_balance': 1700,
                'reserved_operations': 300,
                'status': True
            },
            {
                'id': '7badc8f8-65bc-449a-8cde-855234ac63e1',
                'credentials': 'Kazitsky Jason',
                'current_balance': 200,
                'reserved_operations': 200,
                'status': True
            },
            {
                'id': '5597cc3d-c948-48a0-b711-393edf20d9c0',
                'credentials': 'Пархоменко Антон Александрович',
                'current_balance': 10,
                'reserved_operations': 300,
                'status': True
            },
            {
                'id': '867f0924-a917-4711-939b-90b179a96392',
                'credentials': 'Петечкин Петр Измаилович',
                'current_balance': 1000000,
                'reserved_operations': 1,
                'status': False
            }
        ]
        for item in mock_data:
            Account.objects.create(
                id=item['id'],
                credentials=item['credentials'],
                current_balance=item['current_balance'],
                reserved_operations=item['reserved_operations'],
                is_opened=item['status']
        )