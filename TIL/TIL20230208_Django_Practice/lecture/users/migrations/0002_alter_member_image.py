# Generated by Django 4.1.5 on 2023-02-09 00:42

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=pathlib.PureWindowsPath('C:/Users/yhlee/workspace/django/lecture/media')),
        ),
    ]