from django.contrib import admin

from .models.general_ledger import GeneralLedger  
from .models.general_ledger.admin import GeneralLedgerAdmin 
from .models.chart_account import ChartAccount
from .models.chart_account.admin import ChartAccountAdmin 
from .models.account import Account
from .models.account.admin import AccountAdmin 




admin.site.register(GeneralLedger, GeneralLedgerAdmin)
admin.site.register(ChartAccount, ChartAccountAdmin)
admin.site.register(Account, AccountAdmin)
