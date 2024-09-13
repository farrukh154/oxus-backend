from dynamic_rest.serializers import DynamicModelSerializer

from .model import Report


class ReportSerializer(DynamicModelSerializer):
    class Meta:
        name = 'report'
        model = Report
        fields = (
            'id',
            'report_name',
            'uid',
            'category',
            'description'
        )
