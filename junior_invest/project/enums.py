from django.db.models import TextChoices


class ProjectStatusEnum(TextChoices):

    created = 'created'
    filled = 'filled'
    moderated = 'moderated'
