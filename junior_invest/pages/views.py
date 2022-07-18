from rest_framework import viewsets

from . import models, serializers, filters


class PageViewSet(viewsets.ModelViewSet):

    queryset = models.Page.objects.all()
    serializer_class = serializers.PageSerializer
    filterset_class = filters.PageFilterSet
