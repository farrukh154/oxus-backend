from django.contrib import admin

# Register your models here.

from .models.report.model import Report
from.models.report.admin import ReportAdmin

from .models.report_history.model import ReportHistory
from .models.report_history.admin import ReportHistoryAdmin

admin.site.register(Report, ReportAdmin)
admin.site.register(ReportHistory,ReportHistoryAdmin)