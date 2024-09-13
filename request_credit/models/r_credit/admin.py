from django.contrib.admin import ModelAdmin

from .model import RequestCredit
from common.current_user import set_current_user

class RequestCreditAdmin(ModelAdmin):
    model = RequestCredit
    list_display = (
        'id',
        'created_by',
        'created',
        'customer',
        'status',
        'branch',
        'created_by',
    )
    search_fields = ('name',)
    autocomplete_fields = [
        'status',
        'status_change_by',
        'branch',
        'currency_new',
        'approve_currency_new',
        'created_by',
        'economic_activity',
        'economic_activity_type',
        'credit_purpose',
        'credit_product',
        'rejection_reason',
        'decision_client',
        'customer',
        'underwriter_status',
        'underwriter_status_change_by',
        'client_rejection_reason',
    ]
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        if obj is not None:
            context.update(
                {
                    'request_credit_id': obj.id,
                }
            )
        else:
            context.update({'request_credit_id': 0})
        return super().render_change_form(request, context, add, change, form_url, obj)

    def save_model(self, request, obj, form, change):
        if request.user:
            set_current_user(obj, request.user)
        super().save_model(request, obj, form, change)
