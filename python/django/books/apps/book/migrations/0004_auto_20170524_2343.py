# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-24 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_inprint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='inprint',
            field=models.BooleanField(),
        ),
    ]
