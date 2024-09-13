from dynamic_rest.serializers import DynamicModelSerializer
from dynamic_rest.serializers import DynamicRelationField

from .models import User


class UserSerializer(DynamicModelSerializer):

    class Meta:
        name = "users"

        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'get_full_name',
            'swift_loan_role',
        )


