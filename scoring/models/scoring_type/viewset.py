from dynamic_rest.viewsets import DynamicModelViewSet
from .model import ScoringType
from .serializer import ScoringTypeSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class ScoringTypeViewSet(DynamicModelViewSet):
    queryset = ScoringType.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = ScoringTypeSerializer
