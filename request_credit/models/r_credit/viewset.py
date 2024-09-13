from dynamic_rest.viewsets import DynamicModelViewSet
from request_credit.models.r_credit import RequestCredit
from request_credit.models.r_credit.serializer import RequestCreditSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions
from django.db.models import Q


class RequestCreditViewSet(DynamicModelViewSet):
    queryset = RequestCredit.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = RequestCreditSerializer

    def get_queryset(self, queryset=None):
        queryset = queryset if queryset else RequestCreditViewSet.queryset

        user = self.request.user
        if user.is_superuser:
            return queryset
        if user.is_swift_loan_user:
            return queryset.filter(
                Q(branch_id__in=user.branches.all().values_list("id", flat=True))
                | Q(branch=None)
            )
        return queryset.none()
