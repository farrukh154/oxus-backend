from django.contrib import admin

from .models import Terminal
from .models import Terminal_Vendor

from .models.terminal.admin import TerminalAdmin
from .models.terminal_vendor.admin import TerminalVendorAdmin


admin.site.register(Terminal, TerminalAdmin)
admin.site.register(Terminal_Vendor, TerminalVendorAdmin)
