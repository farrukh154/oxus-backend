from dynamic_rest.viewsets import DynamicModelViewSet
from terminals.models.terminal import Terminal
from terminals.models.terminal.serializer import TerminalSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class TerminalViewSet(DynamicModelViewSet):
    queryset = Terminal.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = TerminalSerializer
