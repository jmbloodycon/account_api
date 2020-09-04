from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient

from ..models import Account
from ..factories import AccountFactory


class TestAccount(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.account = AccountFactory(current_balance=1200)

    def test_add_balance(self):
        """Test top up account balance."""
        data = {
            'money': 200,
            'id': self.account.account_id,
        }

        res = self.client.put(f'/api/add/{self.account.account_id}/', data=data)
        self.assertEqual(res.status_code, 200)

        account = Account.objects.filter(account_id=self.account.account_id).first()
        self.assertEqual(account.current_balance, 1400)

