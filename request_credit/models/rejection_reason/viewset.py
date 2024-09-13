from dynamic_rest.viewsets import DynamicModelViewSet
from request_credit.models.rejection_reason import RejectionReason
from request_credit.models.rejection_reason.serializer import RejectionReasonSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class RejectionReasonViewSet(DynamicModelViewSet):
    queryset = RejectionReason.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = RejectionReasonSerializer
