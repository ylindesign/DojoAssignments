# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='salt',
            field=models.IntegerField(default=3898530539058L),
            preserve_default=False,
        ),
    ]
