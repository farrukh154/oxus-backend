from django.contrib.admin import ModelAdmin

from .model import RejectionReason


class RejectionReasonAdmin(ModelAdmin):
    model = RejectionReason
    list_display = (
        'name',
    )
    search_fields = ('name',)
