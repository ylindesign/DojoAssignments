# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-25 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='author',
        ),
        migrations.AddField(
            model_name='lecture',
            name='description',
            field=models.TextField(default='hey'),
            preserve_default=False,
        ),
    ]
