# Generated by Django 3.0.8 on 2020-08-06 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogpost_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='created',
            field=models.DateTimeField(),
        ),
    ]