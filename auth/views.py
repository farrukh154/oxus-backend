from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as RawTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView as RawTokenObtainPairView


class TokenObtainPairSerializer(RawTokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client_id'] = serializers.JSONField(required=False, allow_null=True)

    def validate(self, attrs):
        result = super().validate(attrs)

        return result

    def get_token(self, user):
        token = super().get_token(user)
        return token


class TokenObtainPairView(RawTokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
