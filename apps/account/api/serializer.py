from rest_framework import serializers

from ..models import Account


class AccountSerializer(serializers.ModelSerializer):
    """Account serializer"""

    class Meta:
        model = Account
        fields = [
            'account_id',
            'full_name',
            'current_balance',
            'holds',
            'status',
        ]
        read_only_fields = [
            'account_id',
        ]
