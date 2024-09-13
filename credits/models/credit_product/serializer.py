from dynamic_rest.serializers import DynamicModelSerializer

from .model import CreditProduct


class CreditProductSerializer(DynamicModelSerializer):
    class Meta:
        name = 'credit_product'
        model = CreditProduct
        fields = (
            'id',
            'name',
            'uid'
        )
