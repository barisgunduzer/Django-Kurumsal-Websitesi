# Generated by Django 3.0.8 on 2020-08-09 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_comment_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
    ]
