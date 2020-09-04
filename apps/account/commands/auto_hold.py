from django.core.management.base import BaseCommand
from ..models import Account, is_operation_possible


class Command(BaseCommand):
    help = 'Substract hold from account balance.'

    def handle(self, *args, **options):
        accounts = Account.objects.all()

        for account in accounts:
            if is_operation_possible(accounts, 0):
                account.current_balance = account.current_balance - account.hold
                account.holds = 0
                account.save()
