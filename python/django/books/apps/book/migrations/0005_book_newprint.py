# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-24 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20170524_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='newprint',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
