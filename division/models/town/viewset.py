from dynamic_rest.viewsets import DynamicModelViewSet
from division.models.town import Town
from division.models.town.serializer import TownSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class TownViewSet(DynamicModelViewSet):
    queryset = Town.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = TownSerializer
