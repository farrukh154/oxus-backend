from dynamic_rest.serializers import DynamicModelSerializer

from .model import RequestStatus


class RequestStatusSerializer(DynamicModelSerializer):
    class Meta:
        name = 'request_status'
        model = RequestStatus
        fields = (
            'id',
            'name',
            'uid',
        )
