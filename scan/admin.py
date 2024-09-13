from django.contrib import admin

# Register your models here.
from .models.customer_scan.model import CustomerScan
from .models.customer_scan.admin import CustomerScanAdmin
from .models.customer_scan_type.model import CustomerScanType
from .models.customer_scan_type.admin import CustomerScanTypeAdmin
from .models.credit_scan.model import CreditScan
from .models.credit_scan.admin import CreditScanAdmin
from .models.credit_scan_type.model import CreditScanType
from .models.credit_scan_type.admin import CreditScanTypeAdmin

admin.site.register(CustomerScan,CustomerScanAdmin)
admin.site.register(CustomerScanType,CustomerScanTypeAdmin)
admin.site.register(CreditScan,CreditScanAdmin)
admin.site.register(CreditScanType,CreditScanTypeAdmin)