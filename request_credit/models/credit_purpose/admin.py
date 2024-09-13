from django.contrib.admin import ModelAdmin

from .model import CreditPurpose


class CreditPurposeAdmin(ModelAdmin):
    model = CreditPurpose
    list_display = (
        'name',
        'code'
    )
    search_fields = ('name',)
