# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-24 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0005_auto_20180524_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='change_or_not',
            field=models.CharField(choices=[('\u65e0', '\u65e0'), ('\u5e93\u623f\u7533\u8bf7', '\u5e93\u623f\u7533\u8bf7'), ('\u5c0f\u5e93\u7533\u8bf7', '\u5c0f\u5e93\u7533\u8bf7'), ('HP\u63d0\u4f9b', 'HP\u63d0\u4f9b'), ('\u7b2c\u4e09\u65b9\u8d2d\u4e70', '\u7b2c\u4e09\u65b9\u8d2d\u4e70')], default='\u65e0', max_length=255),
        ),
        migrations.AlterField(
            model_name='content',
            name='dfe_name',
            field=models.CharField(choices=[('Pro', 'Pro'), ('Esko', 'Esko'), ('PM', 'PM'), ('\u65e0', '\u65e0')], default='Pro', max_length=255),
        ),
    ]
