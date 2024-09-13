from django.contrib import admin

# Register your models here.
from .models import Customer
from .models.customer.admin import CustomerAdmin

admin.site.register(Customer,CustomerAdmin)