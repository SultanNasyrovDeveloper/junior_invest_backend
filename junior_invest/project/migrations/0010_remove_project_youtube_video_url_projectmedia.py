# Generated by Django 4.0.5 on 2022-07-17 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_alter_project_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='youtube_video_url',
        ),
        migrations.CreateModel(
            name='ProjectMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=500)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='project.project')),
            ],
        ),
    ]