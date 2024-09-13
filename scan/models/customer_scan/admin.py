from django.contrib.admin import ModelAdmin

from .model import CustomerScan


class CustomerScanAdmin(ModelAdmin):
    model = CustomerScan
    list_display = (
        'id',
        'file',
        'created',
        'created_by',
        'updated',
        'updated_by',
        'type',
        'abacus_id',
        'description'
    )
    search_fields = ('file',)
    autocomplete_fields = ['created_by','updated_by','type']
