# Generated by Django 5.1.4 on 2025-01-24 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_user_groups_remove_user_is_superuser_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]
