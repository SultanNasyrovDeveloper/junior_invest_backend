from rest_framework import viewsets

from . import models, serializers, filters


class PageViewSet(viewsets.ModelViewSet):

    queryset = models.Page.objects.all()
    serializer_class = serializers.PageSerializer
    filterset_class = filters.PageFilterSet
    permission_classes = []


class TermsFileViewSet(viewsets.ModelViewSet):

    queryset = models.TermsPageFiles.objects.all()
    serializer_class = serializers.TermsFileSerializer
    permission_classes = []
