from dynamic_rest.serializers import DynamicModelSerializer

from .model import RejectionReason


class RejectionReasonSerializer(DynamicModelSerializer):
    class Meta:
        name = 'rejection_reason'
        model = RejectionReason
        fields = (
            'id',
            'name',
        )
