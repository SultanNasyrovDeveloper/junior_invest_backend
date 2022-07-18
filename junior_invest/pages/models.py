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

