from dynamic_rest.serializers import DynamicModelSerializer
from dynamic_rest.serializers import DynamicRelationField

from .model import ClientDecision


class ClientDecisionSerializer(DynamicModelSerializer):
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

    customer = DynamicRelationField(
        "customer.models.customer.serializer.CustomerSerializer",
        label="customer",
    )

    class Meta:
        name = 'client_decision'
        model = ClientDecision
        fields = (
            'id',
            'created_by',
            'updated_by',
            'created',
            'application_receipt_channel',
            'client_decision',
            'customer_response',
            'employee_comments',
            'client_refused',
            'missed_call',
            'customer',
            'active_in_abacus',
        )
