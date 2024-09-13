from dynamic_rest.viewsets import DynamicModelViewSet
from helpdesk.models.helpdesk import Helpdesk
from helpdesk.models.helpdesk.serializer import HelpdeskSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions
from django.db.models import Q
from common.utils import has_permission


class HelpdeskViewSet(DynamicModelViewSet):
    serializer_class = HelpdeskSerializer
    permission_classes = (FullDjangoModelPermissions,)

    def get_queryset(self):
        if has_permission(self.request.user, Helpdesk, 'can-view-all_helpdesk'):
            return Helpdesk.objects.all()
        else:
            return Helpdesk.objects.filter(created_by=self.request.user) | Helpdesk.objects.filter(for_whom=self.request.user)