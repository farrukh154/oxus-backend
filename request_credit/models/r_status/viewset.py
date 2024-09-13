from dynamic_rest.viewsets import DynamicModelViewSet
from request_credit.models.r_status import RequestStatus
from request_credit.models.r_status.serializer import RequestStatusSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class RequestStatusViewSet(DynamicModelViewSet):
    queryset = RequestStatus.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = RequestStatusSerializer
