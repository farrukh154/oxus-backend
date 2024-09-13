from dynamic_rest.serializers import DynamicModelSerializer
from dynamic_rest.serializers import DynamicRelationField
from .model import CreditScanType



class CreditScanTypeSerializer(DynamicModelSerializer):

    class Meta:
        name = 'credit_scan_type'
        model = CreditScanType
        fields = (
            'id',
            'uid',
            'name',
        )
