from django_filters import rest_framework as filters

from . import models


class PageFilterSet(filters.FilterSet):

    class Meta:
        model = models.Page
        fields = '__all__'
