# Generated by Django 4.2.11 on 2024-05-31 15:08

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_alter_post_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(blank=True, default='dfy0one9z', max_length=255, verbose_name='image'),
        ),
    ]
