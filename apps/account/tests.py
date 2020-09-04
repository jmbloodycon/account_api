from django.test import TestCase

from .factories import AccountFactory


class AccountTestCase(TestCase):

    @classmethod
    def setUp(cls):
        """Create new factory account."""
        cls.account = AccountFactory(current_balance=400, hold=0)

    def test_exists_account_fullname(self):
        """Check exists account's full_name"""
        self.assertTrue(hasattr(self.account, 'full_name'))

    def test_top_ap_balance(self):
        """Check top up balance."""
        self.account.top_up_balance(200)

        self.assertEqual(self.account.current_balance, 600)
        self.assertFalse(self.account.top_up_balance(-200))
        self.assertFalse(self.account.top_up_balance('fgkl'))

    def test_subtract_balance(self):
        """Check subtract balance."""
        self.account.subtract(100)

        self.assertEqual(self.account.current_balance, 300)
        self.assertFalse(self.account.subtract(-200))
        self.assertFalse(self.account.subtract('jkdfsgjlk'))
