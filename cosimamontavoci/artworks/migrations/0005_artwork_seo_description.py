# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0004_auto_20160221_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='seo_description',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
    ]
