from django.contrib.admin import ModelAdmin

from .model import ChartAccount


class ChartAccountAdmin(ModelAdmin):
    model = ChartAccount
    list_display = (
        'account_number',
        'name',
        'ru_name', 
        'tj_name',  
    )
    search_fields = ('name', 'ru_name', 'tj_name', 'account_number')