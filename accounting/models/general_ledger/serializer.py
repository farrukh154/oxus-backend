from dynamic_rest.serializers import DynamicModelSerializer
from dynamic_rest.fields import DynamicRelationField
from rest_framework import serializers
from .model import GeneralLedger
from accounting.models.chart_account.serializer import ChartAccountSerializer
from django.utils.translation import gettext_lazy as _


class GeneralLedgerSerializer(DynamicModelSerializer):
    account = DynamicRelationField(
        'accounting.models.chart_account.serializer.ChartAccountSerializer',
        label =_('Account')
    )
    
    class Meta:
        model = GeneralLedger
        fields = (
            'id',
            'name',
            'account'
        )
