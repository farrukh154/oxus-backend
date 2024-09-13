from django.contrib.admin import ModelAdmin

from .model import Currency


class CurrencyAdmin(ModelAdmin):
    model = Currency
    list_display = (
        'name',
        'code',
        'description',
    )
    search_fields = ('name', 'code')
    
  

