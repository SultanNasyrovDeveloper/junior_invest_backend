# Generated by Django 4.0.5 on 2022-07-06 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_remove_project_filled_remove_project_is_moderated'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.TextField(choices=[('created', 'Created'), ('filled', 'Filled'), ('moderated', 'Moderated')], default='created', max_length=20),
        ),
    ]
