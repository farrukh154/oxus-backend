from dynamic_rest.serializers import DynamicModelSerializer

from .model import Helpdesk_Status


class HelpdeskStatusSerializer(DynamicModelSerializer):
    class Meta:
        name = 'helpdesk_status'
        model = Helpdesk_Status
        fields = (
            'id',
            'name',
            'uid'
        )
