from dynamic_rest.serializers import DynamicModelSerializer

from .model import Helpdesk_Priority


class HelpdeskPrioritySerializer(DynamicModelSerializer):
    class Meta:
        name = 'helpdesk_priority'
        model = Helpdesk_Priority
        fields = (
            'id',
            'name',
            'uid'
        )
