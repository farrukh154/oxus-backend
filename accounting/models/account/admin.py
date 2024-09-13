from django.contrib.admin import ModelAdmin

from .model import Account


class AccountAdmin(ModelAdmin):
    model = Account
    list_display = (
        'code',
        'description', 
    )
    search_fields = ('code', 'description')