# Generated by Django 5.1.4 on 2025-01-17 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='members',
            field=models.IntegerField(default=0),
        ),
    ]
