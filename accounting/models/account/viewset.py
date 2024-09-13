from dynamic_rest.viewsets import DynamicModelViewSet
from accounting.models.account import Account
from accounting.models.account.serializer import AccountSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class AccountViewset(DynamicModelViewSet):
    queryset = Account.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = AccountSerializer

