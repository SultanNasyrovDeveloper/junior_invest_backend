from rest_framework import serializers

from . import models


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Page
        fields = '__all__'


class TermsFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TermsPageFiles
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['url'] = representation.pop('file')
        representation['name'] = instance.get_filename()
        return representation
