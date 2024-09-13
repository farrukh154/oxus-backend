from dynamic_rest.serializers import DynamicModelSerializer
from dynamic_rest.serializers import DynamicRelationField
from dynamic_rest.serializers import DynamicRelationField

from .model import Town


class TownSerializer(DynamicModelSerializer):
    region = DynamicRelationField(
        'division.models.region.serializer.RegionSerializer',
        label='region',
    )
    class Meta:
        name = 'town'
        model = Town
        fields = (
            'id',
            'name',
            'region',
            'active',
        )
