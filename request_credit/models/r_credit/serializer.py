from dynamic_rest.serializers import DynamicModelSerializer
from dynamic_rest.serializers import DynamicRelationField
from oxus.utils.try_get_attr import try_get_attr
from common.current_user import set_current_user
from .model import RequestCredit
from django.utils.translation import gettext_lazy as _

class RequestCreditSerializer(DynamicModelSerializer):
    status = DynamicRelationField(
        'request_credit.models.r_status.serializer.RequestStatusSerializer',
        label=_('status'),
    )
    branch = DynamicRelationField(
        'division.models.branch.serializer.BranchSerializer',
        label=_('branch'),
    )
    currency_new = DynamicRelationField(
        'division.models.currency.serializer.CurrencySerializer',
        label=_('currency'),
    )
    approve_currency_new = DynamicRelationField(
        'division.models.currency.serializer.CurrencySerializer',
        label=_('approve currency'),
    )
    created_by = DynamicRelationField(
        'users.serializer.UserSerializer',
        label=_("created by"),
        read_only=True,
    )
    updated_by = DynamicRelationField(
        'users.serializer.UserSerializer',
        label=_("updated by"),
        read_only=True,
    )
    economic_activity = DynamicRelationField(
        'request_credit.models.economic_activity.serializer.EconomicActivitySerializer',
        label=_('economic activity'),
    )
    economic_activity_type = DynamicRelationField(
        'request_credit.models.economic_activity_type.serializer.EconomicActivityTypeSerializer',
        label=_('economic activity type'),
    )
    credit_purpose = DynamicRelationField(
        'request_credit.models.credit_purpose.serializer.CreditPurposeSerializer',
        label=_('credit purpose'),
    )
    status_change_by = DynamicRelationField(
        'users.serializer.UserSerializer',
        label=_('status change by'),
    )
    credit_product = DynamicRelationField(
        'credits.models.credit_product.serializer.CreditProductSerializer',
        label=_('credit product'),
    )
    rejection_reason = DynamicRelationField(
        'request_credit.models.rejection_reason.serializer.RejectionReasonSerializer',
        label=_('rejection reason'),
    )
    client_rejection_reason = DynamicRelationField(
        'request_credit.models.rejection_reason.serializer.RejectionReasonSerializer',
        label=_('client rejection reason'),
    )
    decision_client = DynamicRelationField(
        'request_credit.models.client_decision.serializer.ClientDecisionSerializer',
        label=_('decision client'),
    )

    customer = DynamicRelationField(
        "customer.models.customer.serializer.CustomerSerializer",
        label=_("customer"),
    )

    underwriter_status = DynamicRelationField(
        'request_credit.models.r_status.serializer.RequestStatusSerializer',
        label=_('underwriter status'),
    )
    underwriter_status_change_by = DynamicRelationField(
        'users.serializer.UserSerializer',
        label=_('underwriter status change by'),
    )



    class Meta:
        name = 'request_credit'
        model = RequestCredit
        fields = (
            'created',
            'id',
            'credit_ID',
            'status',
            'branch',
            'created_by',
            'updated_by',
            'family_number',
            'family_number_has_income',
            'current_debt',
            'current_debt_name',
            'acted',
            'full_time_employees',
            'new_job',
            'information_source',
            'economic_activity',
            'economic_activity_type',
            'work_experience',
            'request_amount',
            'currency_new',
            'request_installment',
            'credit_purpose',
            'request_grace_period',
            'investment_sector',
            'activity_location',
            'education',
            'education_info',
            'monthly_income',
            'monthly_income_info',
            'monthly_household_expenses',
            'monthly_household_expenses_info',
            'monthly_payment_loans',
            'monthly_payment_loans_info',
            'monthly_profit_info',
            'total_business_assets',
            'total_business_assets_info',
            'client_capital',
            'client_capital_info',
            'total_household_assets',
            'total_household_assets_info',
            'status_change_date',
            'status_change_by',
            'approve_amount',
            'approve_installment',
            'approve_currency_new',
            'approve_interest',
            'approve_grace_period',
            'approve_issue_fee',
            'credit_product',
            'rating_internal',
            'rating_external',
            'approve_condition',
            'rejection_reason',
            'client_rejection_reason',
            'postponed_info',
            'decision_client',
            'customer',
            'underwriter_status',
            'underwriter_status_change_date',
            'underwriter_status_change_by',
            'result',
        )

    def save(self,**kwargs):
        user = self.context['request'].user
        if try_get_attr(lambda: self.instance.id):
            set_current_user(self.instance, user)
        super().save(**kwargs)


      