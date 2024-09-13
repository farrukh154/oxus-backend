from django.contrib.admin import ModelAdmin

from .model import District


class DistrictAdmin(ModelAdmin):
    model = District
    readonly_fields = ['abacus_id']
    list_display = (
        'id',
        'abacus_id',
        'name',
        'town',
        'active',
    )
    search_fields = ('name',)
    autocomplete_fields = ['town',]
