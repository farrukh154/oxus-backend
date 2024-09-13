from django.contrib.admin import ModelAdmin

from .model import Helpdesk


class HelpdeskAdmin(ModelAdmin):
    model = Helpdesk
    list_display = (
        'id',
        'name',
        'status',
        'priority',
        'branch',
        'created_by',
        'updated_by',
        'for_whom',
    )
    search_fields = ('name',)
    autocomplete_fields = ['status', 'priority', 'branch','created_by','updated_by','for_whom']

