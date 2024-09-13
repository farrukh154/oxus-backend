from django.contrib.admin import ModelAdmin

from .model import EconomicActivity


class EconomicActivityAdmin(ModelAdmin):
    model = EconomicActivity
    list_display = (
        'name',
        'active'
    )
    search_fields = ('name',)
