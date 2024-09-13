from django.contrib.admin import ModelAdmin

from .model import GeneralLedger

class GeneralLedgerAdmin(ModelAdmin):
    model = GeneralLedger
    list_display = (
        'name',
        'account'
    )
    search_fields = ('name', 'account__name')
    autocomplete_fields = [
        'account',
    ]