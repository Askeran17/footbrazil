# Generated by Django 4.2.11 on 2024-05-11 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]
