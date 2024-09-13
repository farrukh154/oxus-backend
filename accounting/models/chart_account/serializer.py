from dynamic_rest.serializers import DynamicModelSerializer

from .model import ChartAccount


class ChartAccountSerializer(DynamicModelSerializer):
    class Meta:
        name = 'chart_account'
        model = ChartAccount
        fields = (
            'name',
            'ru_name',
            'tj_name',
            'account_number'
        )
