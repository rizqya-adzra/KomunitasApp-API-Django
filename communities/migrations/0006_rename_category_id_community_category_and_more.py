# Generated by Django 5.1.4 on 2025-01-17 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0005_community_category_id_community_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='community',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='community',
            old_name='user_id',
            new_name='user',
        ),
    ]
