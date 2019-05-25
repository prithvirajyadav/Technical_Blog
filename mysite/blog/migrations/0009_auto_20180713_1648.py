# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-13 11:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180713_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 13, 11, 18, 2, 181000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 13, 11, 18, 2, 180000, tzinfo=utc)),
        ),
    ]
