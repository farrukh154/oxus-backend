from django.contrib.admin import ModelAdmin

from .model import Helpdesk_Priority


class HelpdeskPriorityAdmin(ModelAdmin):
    model = Helpdesk_Priority
    list_display = (
        'id',
        'name',
    )
    search_fields = ('name',)
