# Generated by Django 2.1.7 on 2019-04-01 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0007_auto_20190325_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='photo_logo',
            field=models.ImageField(blank=True, upload_to='UniPhotos/Logo/'),
        ),
        migrations.AlterField(
            model_name='university',
            name='photo_main',
            field=models.ImageField(blank=True, upload_to='UniPhotos/main/'),
        ),
    ]
