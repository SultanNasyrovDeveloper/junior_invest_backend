from django_filters import rest_framework as filters

from . import models


class ProjectCategoryFilterSet(filters.FilterSet):

    class Meta:
        model = models.ProjectCategory
        fields = '__all__'


class ProjectFilterSet(filters.FilterSet):

    class Meta:
        model = models.Project
        exclude = ('image', 'presentation')


class ProjectVoteFilterSet(filters.FilterSet):

    class Meta:
        model = models.ProjectVote
        fields = '__all__'
