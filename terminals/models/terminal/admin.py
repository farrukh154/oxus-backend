from django.contrib.admin import ModelAdmin

from .model import Terminal


class TerminalAdmin(ModelAdmin):
    model = Terminal
    list_display = (
        'id',
        'name',
    )
    search_fields = ('name',)
