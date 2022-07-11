from django.db.models import Count
from rest_framework import status
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from . import models, serializers, filters, enums


class ProjectCategoryViewSet(viewsets.ModelViewSet):

    queryset = models.ProjectCategory.objects.all()
    serializer_class = serializers.ProjectCategorySerializer
    filterset_class = filters.ProjectCategoryFilterSet


class ProjectViewSet(viewsets.ModelViewSet):

    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    filterset_class = filters.ProjectFilterSet

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.annotate(votes_count=Count('votes'))
        return self.queryset

    def create(self, request, *args, **kwargs) -> Response:
        """
        Create project instance.

        Request user is used as a project author.
        """
        data = dict(request.data)
        user = self.request.user
        if user.projects.filter(status=enums.ProjectStatusEnum.created).count() > 0:
            raise ValidationError('Заполните предыдущий проект перед созданием нового')

        data['author'] = user.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class ProjectImageViewSet(viewsets.ModelViewSet):

    queryset = models.ProjectImage.objects.all()
    serializer_class = serializers.ProjectImageSerializer


class ProjectVoteViewSet(viewsets.ModelViewSet):

    queryset = models.ProjectVote.objects.all()
    serializer_class = serializers.ProjectVoteSerializer
    filterset_class = filters.ProjectVoteFilterSet
