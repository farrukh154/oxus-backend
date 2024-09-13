from django.contrib.admin import ModelAdmin

from .model import Report


class ReportAdmin(ModelAdmin):
    model = Report
    list_display = (
        'id',
        'uid',
        'report_name',
        'description',
        'category',
    )
    search_fields = ('report_name',)
