from django.contrib.admin import ModelAdmin

from .model import ReportHistory


class ReportHistoryAdmin(ModelAdmin):
    model = ReportHistory
    list_display = (
        'id',
        'report',
        'generated_by',
        'created',
        'updated',
        'info',
        'duration',
        'xlsx_report'
    )
    search_fields = ('report',)
    autocomplete_fields = ['report', 'generated_by']
