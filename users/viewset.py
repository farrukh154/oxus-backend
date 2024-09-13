from dynamic_rest.viewsets import DynamicModelViewSet
from .models import User
from .serializer import UserSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions


class UserViewSet(DynamicModelViewSet):
    queryset = User.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = UserSerializer
