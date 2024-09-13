from dynamic_rest.viewsets import DynamicModelViewSet
from division.models.currency.model import Currency
from division.models.currency.serializer import CurrencySerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class CurrencyViewSet(DynamicModelViewSet):
    queryset = Currency.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = CurrencySerializer
