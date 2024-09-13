from dynamic_rest.viewsets import DynamicModelViewSet
from request_credit.models.economic_activity import EconomicActivity
from request_credit.models.economic_activity.serializer import EconomicActivitySerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class EconomicActivityViewSet(DynamicModelViewSet):
    queryset = EconomicActivity.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = EconomicActivitySerializer
