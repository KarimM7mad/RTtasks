# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_isfavourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='albumLogo',
            field=models.FileField(upload_to=''),
        ),
    ]
