from dynamic_rest.viewsets import DynamicModelViewSet
from scan.models.customer_scan_type.model import CustomerScanType
from scan.models.customer_scan_type.serializer import CustomerScanTypeSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class CustomerScanTypeViewSet(DynamicModelViewSet):
    queryset = CustomerScanType.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = CustomerScanTypeSerializer
