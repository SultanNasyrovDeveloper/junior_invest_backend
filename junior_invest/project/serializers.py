from rest_framework import serializers

from . import models


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

    images = ProjectImageSerializer(many=True, required=False)

    class Meta:
        model = models.Project
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.presentation:
            presentation = {
                'url': representation.pop('presentation'),
                'size': instance.presentation.size,
                'name': instance.get_presentation_filename()
            }
            representation['presentation'] = presentation
        return representation
