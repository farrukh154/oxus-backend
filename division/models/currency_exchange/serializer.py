from dynamic_rest.serializers import DynamicModelSerializer
from dynamic_rest.serializers import DynamicRelationField
from .model import CurrencyExchange


class CurrencyExchangeSerializer(DynamicModelSerializer):

    currency_from = DynamicRelationField(
        'division.models.currency.serializer.CurrencySerializer',
        label='currency_from',
    )

    currency_to = DynamicRelationField(
        'division.models.currency.serializer.CurrencySerializer',
        label='currency_to',
    )
    class Meta:
        name = 'currency_exchange'
        model = CurrencyExchange
        fields = (
            'id',
            'date',
            'rate',
            'currency_from',
            'currency_to',
        )
