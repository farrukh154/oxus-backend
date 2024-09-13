from django.contrib import admin

from .models import CRIF
from .models import ScoringType

from .models.crif.admin import CRIFAdmin
from .models.scoring_type.admin import ScoringTypeAdmin

admin.site.register(CRIF, CRIFAdmin)
admin.site.register(ScoringType, ScoringTypeAdmin)
