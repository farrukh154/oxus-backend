from django.contrib.admin import ModelAdmin

from .model import Helpdesk_Status


class HelpdeskStatusAdmin(ModelAdmin):
    model = Helpdesk_Status
    list_display = (
        'id',
        'name',
    )
    search_fields = ('name',)
