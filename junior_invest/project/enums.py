from django.db.models import TextChoices


class ProjectStatusEnum(TextChoices):

    created = 'created', 'Создан'
    filled = 'filled', 'На модерации'
    moderated = 'moderated', 'Прошел модерацию'
