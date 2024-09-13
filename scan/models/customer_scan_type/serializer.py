from dynamic_rest.serializers import DynamicModelSerializer
from dynamic_rest.serializers import DynamicRelationField
from .model import CustomerScanType



class CustomerScanTypeSerializer(DynamicModelSerializer):

    class Meta:
        name = 'customer_scan_type'
        model = CustomerScanType
        fields = (
            'id',
            'uid',
            'name',
        )
