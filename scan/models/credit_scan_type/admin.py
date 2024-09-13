from django.contrib.admin import ModelAdmin

from .model import CreditScanType


class CreditScanTypeAdmin(ModelAdmin):
    model = CreditScanType
    list_display = (
        'id',
        'name',
        'uid',
    )
    search_fields = ('name',)
