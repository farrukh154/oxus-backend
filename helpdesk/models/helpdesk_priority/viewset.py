from dynamic_rest.viewsets import DynamicModelViewSet
from helpdesk.models.helpdesk_priority import Helpdesk_Priority
from helpdesk.models.helpdesk_priority.serializer import HelpdeskPrioritySerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class HelpdeskPriorityViewSet(DynamicModelViewSet):
    queryset = Helpdesk_Priority.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = HelpdeskPrioritySerializer
