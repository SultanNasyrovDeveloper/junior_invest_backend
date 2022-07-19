import os
from datetime import datetime
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from .enums import ProjectStatusEnum


class ProjectCategory(models.Model):

    name = models.CharField(max_length=1000, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория проекта'
        verbose_name_plural = 'Категории проектов'

    def __str__(self):
        return f'[ID={self.id}] - {self.name}'


class ProjectMedia(models.Model):
    project = models.ForeignKey(
        'project.Project',
        on_delete=models.CASCADE,
        related_name='media'
    )
    url = models.URLField(max_length=500, verbose_name='Адрес ресурса')

    class Meta:
        verbose_name = 'Медиа'
        verbose_name_plural = 'Медиа'


class Project(models.Model):

    status = models.TextField(
        max_length=20,
        choices=ProjectStatusEnum.choices,
        default=ProjectStatusEnum.created,
        verbose_name='Статус'
    )
    category = models.ForeignKey(
        'project.ProjectCategory',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория'
    )
    name = models.CharField(
        max_length=1000,
        verbose_name='Название'
    )
    description = models.TextField(
        default='',
        verbose_name='Описание',
    )
    author = models.ForeignKey(
        'user.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='projects',
        verbose_name='Автор'
    )
    presentation = models.FileField(
        upload_to='project_presentations/',
        null=True,
        default=None,
        verbose_name='Презентация'
    )

    created = models.DateTimeField(
        auto_created=True,
        default=datetime.now,
        verbose_name='Дата создания',
    )

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f'[ID={self.id}] - {self.name}'

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

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

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

    class Meta:
        unique_together = ('user', 'project')
        verbose_name = 'Голос'
        verbose_name_plural = 'Голоса'


