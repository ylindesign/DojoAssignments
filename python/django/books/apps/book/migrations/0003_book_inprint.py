# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-24 23:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20170524_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='inprint',
            field=models.BooleanField(default=True),
        ),
    ]