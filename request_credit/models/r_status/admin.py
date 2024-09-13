from django.contrib.admin import ModelAdmin

from .model import RequestStatus


class RequestStatusAdmin(ModelAdmin):
    model = RequestStatus
    list_display = (
        'id',
        'name',
        'uid'
    )
    search_fields = ('name', 'uid')
