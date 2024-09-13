from dynamic_rest.viewsets import DynamicModelViewSet
from helpdesk.models.helpdesk_status import Helpdesk_Status
from helpdesk.models.helpdesk_status.serializer import HelpdeskStatusSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class HelpdeskStatusViewSet(DynamicModelViewSet):
    queryset = Helpdesk_Status.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = HelpdeskStatusSerializer
