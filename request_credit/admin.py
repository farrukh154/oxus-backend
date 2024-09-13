from django.contrib import admin

from .models import RequestCredit
from .models import RequestStatus

from .models.r_credit.admin import RequestCreditAdmin
from .models.r_status.admin import RequestStatusAdmin

from .models.rejection_reason import RejectionReason
from .models.rejection_reason.admin import RejectionReasonAdmin

from .models.credit_purpose import CreditPurpose
from .models.credit_purpose.admin import CreditPurposeAdmin

from .models.economic_activity_type import EconomicActivityType
from .models.economic_activity_type.admin import EconomicActivityTypeAdmin
from .models.economic_activity import EconomicActivity
from .models.economic_activity.admin import EconomicActivityAdmin

from .models.client_decision import ClientDecision
from .models.client_decision.admin import ClientDecisionAdmin



admin.site.register(RequestCredit, RequestCreditAdmin)
admin.site.register(RequestStatus, RequestStatusAdmin)
admin.site.register(RejectionReason, RejectionReasonAdmin)
admin.site.register(CreditPurpose, CreditPurposeAdmin)
admin.site.register(EconomicActivityType, EconomicActivityTypeAdmin)
admin.site.register(EconomicActivity, EconomicActivityAdmin)
admin.site.register(ClientDecision, ClientDecisionAdmin)
