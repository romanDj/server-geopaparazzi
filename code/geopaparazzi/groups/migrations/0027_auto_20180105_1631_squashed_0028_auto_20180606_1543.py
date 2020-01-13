# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-04 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('groups', '0027_auto_20180105_1631'), ('groups', '0028_auto_20180606_1543')]

    dependencies = [
        ('groups', '26_to_27'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='groupinvitation',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='groupinvitation',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='groupinvitation',
            name='group',
        ),
        migrations.RemoveField(
            model_name='groupinvitation',
            name='user',
        ),
        migrations.DeleteModel(
            name='GroupInvitation',
        ),
        migrations.AlterField(
            model_name='groupcategory',
            name='description',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='groupcategory',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='groupcategory',
            name='name_en',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='groupprofile',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='groups', to='groups.GroupCategory', verbose_name='Categories'),
        ),
    ]
