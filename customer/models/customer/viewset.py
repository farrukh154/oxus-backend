from dynamic_rest.viewsets import DynamicModelViewSet

from customer.models.customer import Customer
from customer.models.customer.serializer import CustomerSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions

class CustomerViewSet(DynamicModelViewSet):
    queryset = Customer.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = CustomerSerializer
