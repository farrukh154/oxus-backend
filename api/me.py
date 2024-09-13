
from rest_framework import status
from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import User
from rest_framework import serializers
from api.model_name_to_entity_name import get_entity_name
from rest_framework.fields import SerializerMethodField

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        name = 'user'
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'is_swift_loan_user',
            'swift_loan_role',
            'permissions',
            'is_superuser',
        )

    permissions = SerializerMethodField(label='permissions')

    @staticmethod
    def get_permissions(user: User):
        result = {}
        for full_permission in user.get_all_permissions():
            app, permission = full_permission.split('.')
            operation, model_name = permission.split('_', 1)
            entity_name = get_entity_name(app, model_name)
            # just skipping models without corresponding entity name, i.e. models that are not registered in router
            if entity_name is not None:
                operations = result.setdefault(entity_name, set())
                assert operation not in operations
                operations.add(operation)
        return result

class MeView(views.APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)