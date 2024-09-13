from django.contrib.admin import ModelAdmin

from .model import CustomerScanType


class CustomerScanTypeAdmin(ModelAdmin):
    model = CustomerScanType
    list_display = (
        'id',
        'name',
        'uid',
    )
    search_fields = ('name',)
