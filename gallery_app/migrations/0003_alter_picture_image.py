# Generated by Django 4.1.3 on 2022-12-10 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0002_picture_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(default=0, upload_to='pictures/'),
            preserve_default=False,
        ),
    ]
