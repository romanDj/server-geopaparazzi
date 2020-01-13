# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-03-09 08:37


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0030_auto_20180309_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='bbox_x0',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='bbox_x1',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='bbox_y0',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='bbox_y1',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='bbox_x0',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='bbox_x1',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='bbox_y0',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='bbox_y1',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True),
        ),
    ]
