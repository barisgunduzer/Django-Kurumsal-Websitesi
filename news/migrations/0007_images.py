# Generated by Django 3.0.8 on 2020-07-26 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20200726_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Post')),
            ],
        ),
    ]