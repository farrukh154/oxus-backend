from dynamic_rest.viewsets import DynamicModelViewSet
from division.models.region import Region
from division.models.region.serializer import RegionSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class RegionViewSet(DynamicModelViewSet):
    queryset = Region.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = RegionSerializer
