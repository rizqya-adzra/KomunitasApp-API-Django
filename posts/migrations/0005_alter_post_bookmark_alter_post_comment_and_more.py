# Generated by Django 5.1.4 on 2025-01-20 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_bookmark_alter_post_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bookmark',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
