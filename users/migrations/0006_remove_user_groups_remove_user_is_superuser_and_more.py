# Generated by Django 5.1.4 on 2025-01-20 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_groups_user_is_active_user_is_superuser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
    ]
