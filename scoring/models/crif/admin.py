from django.contrib.admin import ModelAdmin

from .model import CRIF


class CRIFAdmin(ModelAdmin):
    model = CRIF

    list_display = (
        'id',
        'created',
        'generated_by',
        'type',
        'parent',
        'crif_credit_id'
    )
    search_fields = ('id',)
    autocomplete_fields = [
        'generated_by',
        'request_credit',
        'type',
        'parent',
    ]
