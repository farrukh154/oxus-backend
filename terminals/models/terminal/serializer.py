from dynamic_rest.serializers import DynamicModelSerializer

from .model import Terminal


class TerminalSerializer(DynamicModelSerializer):
    class Meta:
        name = 'terminal'
        model = Terminal
        fields = (
            'id',
            'name',
        )
