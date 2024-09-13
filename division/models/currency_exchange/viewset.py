from dynamic_rest.viewsets import DynamicModelViewSet
from division.models.currency_exchange.model import CurrencyExchange
from division.models.currency_exchange.serializer import CurrencyExchangeSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class CurrencyExchangeViewSet(DynamicModelViewSet):
    queryset = CurrencyExchange.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = CurrencyExchangeSerializer
