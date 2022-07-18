from rest_framework import serializers

from junior_invest.user.serializers import SimpleUserSerializer

from . import models


class ProjectMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProjectMedia
        fields = '__all__'


class ProjectCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProjectCategory
        fields = '__all__'


class ProjectImageSerializer(serializers.ModelSerializer):

    thumbnail = serializers.ImageField(required=False)

    class Meta:
        model = models.ProjectImage
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['file'] = {
            'url': representation.pop('file'),
            'size': instance.file.size,
            'name': instance.get_filename()
        }
        return representation


class ProjectVoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProjectVote
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):

    media = ProjectMediaSerializer(many=True)
    images = ProjectImageSerializer(many=True, required=False)
    votes_count = serializers.IntegerField(required=False)

    class Meta:
        model = models.Project
        fields = '__all__'

    def create(self, validated_data):
        project = super().create(validated_data)
        return project

    def update(self, instance, validated_data):
        if 'media' in validated_data:
            media = validated_data.pop('media')
            instance.media.all().delete()
            instances = [
                models.ProjectMedia(project=instance, url=media_data['url'])
                for media_data in media
            ]
            models.ProjectMedia.objects.bulk_create(instances)
        return super().update(instance, validated_data)

    def to_representation(self, project):
        representation = super().to_representation(project)
        if project.presentation:
            presentation = {
                'url': representation.pop('presentation'),
                'size': project.presentation.size,
                'name': project.get_presentation_filename()
            }
            representation['presentation'] = presentation
        representation['author'] = SimpleUserSerializer(project.author).data
        return representation
