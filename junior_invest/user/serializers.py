from djoser.serializers import (
    UserCreateSerializer as DjoserUserCreateSerializer
)
from rest_framework import serializers

from . import models


class UserSerializer(DjoserUserCreateSerializer):

    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta(DjoserUserCreateSerializer.Meta):
        model = models.User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
