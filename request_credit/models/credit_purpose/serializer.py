from dynamic_rest.serializers import DynamicModelSerializer

from .model import CreditPurpose


class CreditPurposeSerializer(DynamicModelSerializer):
    class Meta:
        name = 'credit_purpose'
        model = CreditPurpose
        fields = (
            'name',
            'code',
            'id'
        )
