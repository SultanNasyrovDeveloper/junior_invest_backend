# Generated by Django 4.0.5 on 2022-07-19 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_alter_project_options_alter_projectcategory_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectcategory',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='project_category_images/'),
        ),
    ]