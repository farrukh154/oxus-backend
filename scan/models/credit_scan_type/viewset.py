from dynamic_rest.viewsets import DynamicModelViewSet
from scan.models.credit_scan_type.model import CreditScanType
from scan.models.credit_scan_type.serializer import CreditScanTypeSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class CreditScanTypeViewSet(DynamicModelViewSet):
    queryset = CreditScanType.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = CreditScanTypeSerializer
