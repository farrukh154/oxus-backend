from dynamic_rest.viewsets import DynamicModelViewSet
from request_credit.models.credit_purpose import CreditPurpose
from request_credit.models.credit_purpose.serializer import CreditPurposeSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class CreditPurposeViewSet(DynamicModelViewSet):
    queryset = CreditPurpose.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = CreditPurposeSerializer
