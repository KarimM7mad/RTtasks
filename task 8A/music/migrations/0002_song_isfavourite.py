# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='isFavourite',
            field=models.BooleanField(default=False),
        ),
    ]
