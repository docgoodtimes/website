# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0005_artwork_seo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='seo_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
