# Generated by Django 3.0.8 on 2020-08-01 10:09

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200731_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='ourmission',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='ourvision',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
