from dynamic_rest.serializers import DynamicModelSerializer
from dynamic_rest.serializers import DynamicRelationField
from .model import CustomerScan




class CustomerScanSerializer(DynamicModelSerializer):

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
        "scan.models.customer_scan_type.serializer.CustomerScanTypeSerializer",
        label = "type"
    )

    class Meta:
        name = 'customer_scan'
        model = CustomerScan
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
