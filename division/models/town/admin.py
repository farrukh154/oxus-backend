from django.contrib.admin import ModelAdmin

from .model import Town


class TownAdmin(ModelAdmin):
    model = Town
    readonly_fields = ['abacus_id']
    list_display = (
        'id',
        'abacus_id',
        'name',
        'region',
        'active',
    )
    search_fields = ('name',)
    autocomplete_fields = ['region',]
