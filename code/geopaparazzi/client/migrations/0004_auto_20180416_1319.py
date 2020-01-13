# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-16 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geonode_client', '0003_geonodethemecustomization_jumbotron_welcome_hide'),
    ]

    operations = [
        migrations.AddField(
            model_name='geonodethemecustomization',
            name='jumbotron_site_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='geonodethemecustomization',
            name='jumbotron_welcome_content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='geonodethemecustomization',
            name='jumbotron_welcome_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
