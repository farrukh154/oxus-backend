from dynamic_rest.viewsets import DynamicModelViewSet
from scan.models.credit_scan.model import CreditScan
from scan.models.credit_scan.serializer import CreditScanSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class CreditScanViewSet(DynamicModelViewSet):
    queryset = CreditScan.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = CreditScanSerializer
