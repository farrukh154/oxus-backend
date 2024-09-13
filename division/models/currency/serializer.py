from dynamic_rest.serializers import DynamicModelSerializer

from .model import Currency


class CurrencySerializer(DynamicModelSerializer):
    class Meta:
        name = 'currency'
        model = Currency
        fields = (
            'id',
            'name',
            'description',
            'uid'
        )
