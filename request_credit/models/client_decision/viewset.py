from dynamic_rest.viewsets import DynamicModelViewSet
from .model import ClientDecision
from .serializer import ClientDecisionSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class ClientDecisionViewSet(DynamicModelViewSet):
    queryset = ClientDecision.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = ClientDecisionSerializer
