# Generated by Django 4.1.5 on 2023-02-06 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='imagefile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
