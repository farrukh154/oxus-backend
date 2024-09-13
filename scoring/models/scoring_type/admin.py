from django.contrib.admin import ModelAdmin

from .model import ScoringType


class ScoringTypeAdmin(ModelAdmin):
    model = ScoringType

    list_display = (
        "id",
        "name",
        "uid",
    )
    search_fields = ("id",)
