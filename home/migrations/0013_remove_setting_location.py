# Generated by Django 3.0.8 on 2020-08-10 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_setting_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='location',
        ),
    ]