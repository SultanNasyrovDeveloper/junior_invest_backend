from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers


class GetMeView(APIView):

    permission_classes = []

    def get(self, request, *args, **kwargs):
        return Response(
            serializers.UserSerializer(request.user).data
        )
