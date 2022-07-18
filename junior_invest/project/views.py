from django.db.models import Count
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from . import models, serializers, filters, enums


class ProjectCategoryViewSet(viewsets.ModelViewSet):

    queryset = models.ProjectCategory.objects.all()
    serializer_class = serializers.ProjectCategorySerializer
    filterset_class = filters.ProjectCategoryFilterSet
    permission_classes = []


class ProjectViewSet(viewsets.ModelViewSet):

    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    filterset_class = filters.ProjectFilterSet

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return []
        return super().get_permissions()

    def get_queryset(self):
        if self.action in ('list', 'retrieve'):
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
        serializer.save()

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


class ProjectMediaViewSet(viewsets.ModelViewSet):

    queryset = models.ProjectMedia.objects.all()
    serializer_class = serializers.ProjectMediaSerializer

    @action(detail=False, methods=('POST', ))
    def create_bulk(self, request, *args, **kwargs):
        data = request.data
        media_objects = []
        for data_object in data.get('media', []):
            serializer = serializers.ProjectMediaSerializer(data=data_object)
            serializer.is_valid(True)
            media_objects.append(models.ProjectMedia(**serializer.validated_data))
        models.ProjectMedia.objects.bulk_create(media_objects)
        return Response({'status': 'success'})


