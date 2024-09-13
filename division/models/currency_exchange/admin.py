from django.contrib.admin import ModelAdmin

from .model import CurrencyExchange


class CurrencyExchangeAdmin(ModelAdmin):
    model = CurrencyExchange
    list_display = (
        'id',
        'date',
        'rate',
        'currency_from',
        'currency_to',
    )
    search_fields = ('currency_from', 'currency_to')
    autocomplete_fields = ['currency_from', 'currency_to']
