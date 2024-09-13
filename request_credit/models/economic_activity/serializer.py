from dynamic_rest.serializers import DynamicModelSerializer

from .model import EconomicActivity


class EconomicActivitySerializer(DynamicModelSerializer):
    class Meta:
        name = 'economic_activity'
        model = EconomicActivity
        fields = (
            'name',
            'active',
            'id'
        )
