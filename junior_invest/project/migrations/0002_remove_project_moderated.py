# Generated by Django 4.0.5 on 2022-07-02 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='moderated',
        ),
    ]
