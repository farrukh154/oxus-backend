from django.contrib.admin import ModelAdmin

from .model import Terminal_Vendor


class TerminalVendorAdmin(ModelAdmin):
    model = Terminal_Vendor
    list_display = (
        "id",
        "name",
    )
    search_fields = ("name",)
