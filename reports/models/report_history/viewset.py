from dynamic_rest.viewsets import DynamicModelViewSet
from reports.models.report_history.model import ReportHistory
from reports.models.report_history.serializer import ReportHistorySerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions
from common.utils import has_permission


class ReportHistoryViewSet(DynamicModelViewSet):
    queryset = ReportHistory.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = ReportHistorySerializer

    def get_queryset(self):
        if has_permission(self.request.user, ReportHistory, 'can-view-all-generated-report_reporthistory'):
            return ReportHistory.objects.all()
        else:
            return ReportHistory.objects.filter(generated_by=self.request.user)
