from dynamic_rest.viewsets import DynamicModelViewSet
from request_credit.models.economic_activity_type import EconomicActivityType
from request_credit.models.economic_activity_type.serializer import EconomicActivityTypeSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class EconomicActivityTypeViewSet(DynamicModelViewSet):
    queryset = EconomicActivityType.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = EconomicActivityTypeSerializer
