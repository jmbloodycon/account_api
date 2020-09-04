import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = (
    'Account',
    'is_operation_possible',
)


class Account(models.Model):
    """Subscriber account model.

    Attributes:
        account_id (str): account number, unique for all accounts.
        full_name (str): the last name, first name of user.
        current_balance (int): current funds on the subscriber's account
        hold (int): reserved for the operation on the account
        status (bool): determines the ability to conduct transactions.

    """
    account_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("Account id")
    )
    full_name = models.CharField(
        max_length=255,
        verbose_name=_("Username")

    )
    current_balance = models.IntegerField(
        default=0,
        verbose_name=_("Current balance"),
    )
    hold = models.IntegerField(
        default=0,
        verbose_name=_("Holds"),
    )
    status = models.BooleanField(
        default=True,
        verbose_name=_("Is active"),

    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Date of creation"),
    )

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Account")

    def __repr__(self):
        return f'{self.full_name} {self.current_balance} {self.status}'

    def top_up_balance(self, replenishment):
        """Add a certain amount to the account.

        Return whether the operation completed successfully.
        """
        try:
            replenishment = int(replenishment)
        except ValueError:
            return False

        if replenishment > 0 and self.status:
            self.current_balance += replenishment
            self.save()
            return True

    def subtract(self, debited):
        """Subtrsct a certain amount from the account.

        Return whether the operation completed successfully.
        """
        try:
            debited = int(debited)
        except ValueError:
            return False

        if debited < 0:
            return False

        if is_operation_possible(self, debited):
            self.current_balance = self.current_balance - debited
            self.save()
            return True


def is_operation_possible(account, substraction):
    """Check whether this operation is possible by condition.

    Possible if the size of the hold + the amount of deduction is less
    than the balance on the subscriber's account.
    """
    return (
            account.current_balance - account.hold - substraction >= 0 and
            account.status
    )
