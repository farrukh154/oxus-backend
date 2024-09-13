from dynamic_rest.serializers import DynamicModelSerializer

from .model import Account


class AccountSerializer(DynamicModelSerializer):
    class Meta:
        name = 'account'
        model = Account
        fields = (
            'code',
            'description'
        )
