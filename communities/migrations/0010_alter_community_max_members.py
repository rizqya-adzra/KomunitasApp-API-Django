# Generated by Django 5.1.4 on 2025-01-17 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0009_alter_community_description_alter_community_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='max_members',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
