from dynamic_rest.viewsets import DynamicModelViewSet
from reports.models.report.model import Report
from reports.models.report.serializer import ReportSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class ReportViewSet(DynamicModelViewSet):
    queryset = Report.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = ReportSerializer
