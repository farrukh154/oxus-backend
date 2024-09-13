from dynamic_rest.serializers import DynamicModelSerializer
from dynamic_rest.serializers import DynamicRelationField

from .model import District



class DistrictSerializer(DynamicModelSerializer):
    town = DynamicRelationField(
        'division.models.town.serializer.TownSerializer',
        label='town',
    )
    class Meta:
        name = 'district'
        model = District
        fields = (
            'id',
            'name',
            'town',
            'active',
            'abacus_id',
        )
