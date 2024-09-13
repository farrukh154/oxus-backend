from django.contrib.admin import ModelAdmin

from .model import EconomicActivityType


class EconomicActivityTypeAdmin(ModelAdmin):
    model = EconomicActivityType
    list_display = (
        'name',
        'active',
        'economic_activity'
    )
    search_fields = ('name',)
    autocomplete_fields = ['economic_activity']

