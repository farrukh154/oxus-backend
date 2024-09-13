from django.contrib.admin import ModelAdmin

from .model import Region


class RegionAdmin(ModelAdmin):
    model = Region
    change_list_template = "change_list.html"
    readonly_fields = ["abacus_id"]
    list_display = (
        "id",
        "abacus_id",
        "name",
        "active",
    )
    search_fields = ("name",)
