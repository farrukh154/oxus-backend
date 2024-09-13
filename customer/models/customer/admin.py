from django.contrib.admin import ModelAdmin

from .model import Customer


class CustomerAdmin(ModelAdmin):
    model = Customer

    list_display = (
        'id',
        'name',
        'birthday',
        'gender',
        'client_ID',
        'INN',
        'passport',
        'branch',
        'registration_address',
        'address',
        'family_status',
        'spouse',
        'spouse_phone'
    )
    search_fields = ('name',)

    autocomplete_fields = [
        'branch',
        'registration_address',
        'address',
    ]
