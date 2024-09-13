from django.contrib import admin

from .models.branch import Branch
from .models.branch.admin import BranchAdmin

from .models.region import Region
from .models.region.admin import RegionAdmin

from .models.town.admin import TownAdmin
from .models.town import Town

from .models.district.admin import DistrictAdmin
from .models.district import District

from .models.currency.admin import CurrencyAdmin
from .models.currency import Currency

from .models.currency_exchange.admin import CurrencyExchangeAdmin
from .models.currency_exchange import CurrencyExchange

admin.site.register(Branch,BranchAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(Town,TownAdmin)
admin.site.register(District,DistrictAdmin)
admin.site.register(Currency,CurrencyAdmin)
admin.site.register(CurrencyExchange,CurrencyExchangeAdmin)