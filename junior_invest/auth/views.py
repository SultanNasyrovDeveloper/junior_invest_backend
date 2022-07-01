from rest_framework_simplejwt.views import TokenObtainPairView

from . import serializers


class TokenPairObtainView(TokenObtainPairView):
    serializer_class = serializers.TokenPairObtainSerializer
