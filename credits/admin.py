from django.contrib import admin

from .models.credit_product import CreditProduct

from .models.credit_product.admin import CreditProductAdmin


admin.site.register(CreditProduct, CreditProductAdmin)
