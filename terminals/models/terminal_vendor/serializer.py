from dynamic_rest.serializers import DynamicModelSerializer

from .model import Terminal_Vendor


class TerminalVendorSerializer(DynamicModelSerializer):
    class Meta:
        name = "terminal_vendor"
        model = Terminal_Vendor
        fields = (
            "id",
            "name",
        )
