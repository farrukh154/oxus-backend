from dynamic_rest.viewsets import DynamicModelViewSet
from scan.models.customer_scan.model import CustomerScan
from scan.models.customer_scan.serializer import CustomerScanSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class CustomerScanViewSet(DynamicModelViewSet):
    queryset = CustomerScan.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = CustomerScanSerializer
