from dynamic_rest.viewsets import DynamicModelViewSet
from accounting.models.chart_account import ChartAccount
from accounting.models.chart_account.serializer import ChartAccountSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class ChartAccountViewSet(DynamicModelViewSet):
    queryset = ChartAccount.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = ChartAccountSerializer

