from django.contrib.admin import ModelAdmin

from .model import CreditProduct


class CreditProductAdmin(ModelAdmin):
    model = CreditProduct
    list_display = (
        'id',
        'name',
    )
    search_fields = ('name',)
