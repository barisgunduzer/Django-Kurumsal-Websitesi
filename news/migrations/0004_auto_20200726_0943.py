# Generated by Django 3.0.8 on 2020-07-26 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200726_0847'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News',
            new_name='Posts',
        ),
    ]