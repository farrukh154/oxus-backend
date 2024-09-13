from dynamic_rest.viewsets import DynamicModelViewSet
from .model import CRIF
from .serializer import CRIFSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class CRIFViewSet(DynamicModelViewSet):
    queryset = CRIF.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = CRIFSerializer
