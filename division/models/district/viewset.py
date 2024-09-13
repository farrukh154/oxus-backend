from dynamic_rest.viewsets import DynamicModelViewSet
from division.models.district import District
from division.models.district.serializer import DistrictSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class DistrictViewSet(DynamicModelViewSet):
    queryset = District.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = DistrictSerializer
