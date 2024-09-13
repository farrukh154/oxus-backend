from dynamic_rest.viewsets import DynamicModelViewSet
from terminals.models.terminal_vendor import Terminal_Vendor
from terminals.models.terminal_vendor.serializer import TerminalVendorSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class TerminalVendorViewSet(DynamicModelViewSet):
    queryset = Terminal_Vendor.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = TerminalVendorSerializer
