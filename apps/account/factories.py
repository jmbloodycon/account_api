import factory
from random import randint

from .models import Account

__all__ = (
    'AccountFactory'
)


class AccountFactory(factory.DjangoModelFactory):
    """Generate account with full_name, current_balance and hold."""
    full_name = factory.Faker('first_name')
    current_balance = randint(100, 2000)
    hold = randint(1, 12)

    class Meta:
        model = Account
