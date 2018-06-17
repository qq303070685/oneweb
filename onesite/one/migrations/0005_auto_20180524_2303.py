# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-24 15:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0004_auto_20180524_2226'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['-date'], 'verbose_name': '\u65e5\u62a5', 'verbose_name_plural': '\u65e5\u62a5'},
        ),
        migrations.AlterField(
            model_name='content',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='content',
            name='change_or_not',
            field=models.IntegerField(choices=[('\u65e0', '\u65e0'), ('\u5e93\u623f\u7533\u8bf7', '\u5e93\u623f\u7533\u8bf7'), ('\u5c0f\u5e93\u7533\u8bf7', '\u5c0f\u5e93\u7533\u8bf7'), ('HP\u63d0\u4f9b', 'HP\u63d0\u4f9b'), ('\u7b2c\u4e09\u65b9\u8d2d\u4e70', '\u7b2c\u4e09\u65b9\u8d2d\u4e70')], default=1),
        ),
        migrations.AlterField(
            model_name='content',
            name='dfe_name',
            field=models.CharField(choices=[('Pro', 'Pro'), ('Esko', 'Esko'), ('PM', 'PM'), ('\u65e0', '\u65e0')], default='2', max_length=255),
        ),
        migrations.AlterField(
            model_name='content',
            name='question',
            field=models.CharField(max_length=255, verbose_name='\u95ee\u9898\u63cf\u8ff0'),
        ),
    ]