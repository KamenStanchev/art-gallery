# Generated by Django 4.1.3 on 2022-12-20 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0013_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=600)),
                ('is_used', models.BooleanField(default=False)),
            ],
        ),
    ]
