from dynamic_rest.viewsets import DynamicModelViewSet
from .model import CreditProduct
from .serializer import CreditProductSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class CreditProductViewSet(DynamicModelViewSet):
    queryset = CreditProduct.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = CreditProductSerializer
