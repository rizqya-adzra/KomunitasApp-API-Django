# Generated by Django 5.1.4 on 2025-01-17 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0003_alter_community_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='category',
        ),
        migrations.RemoveField(
            model_name='community',
            name='user',
        ),
    ]
