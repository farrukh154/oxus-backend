from dynamic_rest.serializers import DynamicModelSerializer
from dynamic_rest.serializers import DynamicRelationField
from .model import CreditScan




class CreditScanSerializer(DynamicModelSerializer):

    created_by = DynamicRelationField(
        "users.serializer.UserSerializer",
        label="Created by",
        read_only=True,
    )

    updated_by = DynamicRelationField(
        "users.serializer.UserSerializer",
        label="Updated by",
        read_only=True,
    )
    type = DynamicRelationField(
        "scan.models.credit_scan_type.serializer.CreditScanTypeSerializer",
        label = "type"
    )

    class Meta:
        name = 'credit_scan'
        model = CreditScan
        fields = (
            'id',
            'file',
            'created',
            'created_by',
            'updated',
            'updated_by',
            'type',
            'abacus_id',
            'description'
        )
