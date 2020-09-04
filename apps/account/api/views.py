from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import UpdateModelMixin

from .serializer import AccountSerializer
from ..models import Account


def get_data_dict(
        http_status: int,
        result: bool,
        addition: dict,
        description: dict
):
    """Return data dict with status code, result, addition."""
    return {
        'status': http_status,
        'result': result,
        'addition': addition,
        'description': description,
    }


def get_addition(account):
    """Return dict addition with id, balance and name account."""
    return {
        'id': account.account_id,
        'balance': account.current_balance,
        'full_name': account.full_name,
    }


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def ping(request, format=None):
    """Check serviceability.

    Return 200 OK with data.
    """
    data = get_data_dict(200, True, {}, {})
    return Response(data)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def status(request, format=None):
    """Return status of account and current balance.

    Implies that the request contains the field 'id'.
    """
    account = Account.objects.filter(account_id=request.data['id']).first()
    addition = {
        'balance': account.current_balance,
        'status': account.status,
    }
    return Response(get_data_dict(200, True, addition, {}))


class TopUpBalanceView(UpdateModelMixin, GenericViewSet):
    """API endpoint that top up account balance if possible."""
    renderer_classes = (JSONRenderer,)
    model = Account
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def update(self, request, *args, **kwargs):
        """Top up account balance if possible.

        Implies that the request contains the fields 'money' and 'id'.
        """
        money = request.data['money']
        account = Account.objects.filter(account_id=request.data['id']).first()

        if account.top_up_balance(money):
            addition = get_addition(account)
            data = get_data_dict(202, True, addition, {})
            return Response(data)

        return Response(get_data_dict(400, False, {}, {}))


class SubstractBalanceView(UpdateModelMixin, GenericViewSet):
    """API endpoint that decrease balance if possible."""
    renderer_classes = (JSONRenderer,)
    model = Account
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def update(self, request, *args, **kwargs):
        """Decrease balance if possible.

        Implies that the request contains the fields 'money' and 'id'.
        """
        money = request.data['money']
        account = Account.objects.filter(account_id=request.data['id']).first()

        if account.subtract(money):
            addition = get_addition(account)
            data = get_data_dict(202, True, addition, {})
            return Response(data)

        return Response(get_data_dict(400, False, {}, {}))
