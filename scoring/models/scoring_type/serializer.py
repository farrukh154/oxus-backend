from dynamic_rest.serializers import DynamicModelSerializer

from .model import ScoringType


class ScoringTypeSerializer(DynamicModelSerializer):

    class Meta:
        name = "scoringtype"

        model = ScoringType
        fields = (
            'id',
            'name',
            "uid",
        )
