from dynamic_rest.viewsets import DynamicModelViewSet
from accounting.models.general_ledger import GeneralLedger
from accounting.models.general_ledger.serializer import GeneralLedgerSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class GeneralLedgerViewSet(DynamicModelViewSet):
    queryset = GeneralLedger.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = GeneralLedgerSerializer

