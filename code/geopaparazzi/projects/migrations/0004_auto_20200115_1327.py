# Generated by Django 2.2.9 on 2020-01-15 13:27

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200115_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 15, 13, 26, 16, 420725), verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='project',
            name='edit_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=300, verbose_name='краткое описание'),
        ),
        migrations.AlterField(
            model_name='subdivision',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 15, 13, 26, 16, 419459), verbose_name='Дата создания'),
        ),
    ]
