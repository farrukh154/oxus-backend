from dynamic_rest.serializers import DynamicModelSerializer
from dynamic_rest.serializers import DynamicRelationField
from .model import EconomicActivityType


class EconomicActivityTypeSerializer(DynamicModelSerializer):
    economic_activity = DynamicRelationField(
        'request_credit.models.economic_activity_type.serializer.EconomicActivityTypeSerializer',
        label='economic_activity',
    )
    class Meta:
        name = 'economic_activity_type'
        model = EconomicActivityType
        fields = (
            'name',
            'active',
            'economic_activity',
            'id'
        )
