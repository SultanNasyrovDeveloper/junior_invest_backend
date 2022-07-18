import os
from datetime import datetime
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from .enums import ProjectStatusEnum


class ProjectCategory(models.Model):

    name = models.CharField(max_length=1000)


class ProjectMedia(models.Model):
    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='media'
    )
    url = models.URLField(max_length=500)


class Project(models.Model):

    status = models.TextField(
        max_length=20,
        choices=ProjectStatusEnum.choices,
        default=ProjectStatusEnum.created
    )
    category = models.ForeignKey(
        'project.ProjectCategory',
        on_delete=models.SET_NULL,
        null=True
    )
    name = models.CharField(max_length=1000)
    description = models.TextField(default='')
    author = models.ForeignKey(
        'user.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='projects'
    )
    presentation = models.FileField(
        upload_to='project_presentations/',
        null=True,
        default=None
    )

    created = models.DateTimeField(auto_created=True, default=datetime.now)

    def get_presentation_filename(self):
        return os.path.basename(self.presentation.name)


class ProjectImage(models.Model):

    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='images'
    )
    file = models.ImageField(upload_to='project_images/')
    thumbnail = avatar_thumbnail = ImageSpecField(
        source='file',
        processors=[ResizeToFill(400, 300)],
        format='JPEG',
        options={'quality': 100}
    )

    def get_filename(self):
        return os.path.basename(self.file.name)


class ProjectVote(models.Model):

    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='project_votes'
    )
    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='votes'
    )


