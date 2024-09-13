from dynamic_rest.serializers import DynamicModelSerializer

from .model import Region


class RegionSerializer(DynamicModelSerializer):
    class Meta:
        name = 'region'
        model = Region
        fields = (
            'id',
            'name',
            'active',
        )
