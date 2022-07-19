import os

from django.db import models
from ckeditor.fields import RichTextField


class Page(models.Model):

    url = models.CharField(max_length=500)
    content = RichTextField()

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return f'Страница: {self.url}'


class TermsPageFiles(models.Model):

    file = models.FileField(upload_to='terms_files/')

    class Meta:
        verbose_name = 'Файл страницы правил'
        verbose_name_plural = 'Файлы страницы правил'

    def get_filename(self):
        return os.path.basename(self.file.name)
