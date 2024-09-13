from django.contrib.admin import ModelAdmin

from .model import ClientDecision


class ClientDecisionAdmin(ModelAdmin):
    model = ClientDecision
    list_display = (
        'id',
        'created_by',
        'updated_by',
        'created',
        'updated',
        'client_refused',
        'missed_call',
    )
    search_fields = (
        'id',
        'created_by',
        'updated_by',
        'status',
        'application_receipt_channel',
        'client_decision',
        'customer_response',
        'employee_comments',
        'client_refused',
        'missed_call',
    )
    autocomplete_fields = ['customer']

