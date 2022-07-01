from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from junior_invest.user.serializers import UserSerializer


class TokenPairObtainSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = UserSerializer(self.user).data
        return data