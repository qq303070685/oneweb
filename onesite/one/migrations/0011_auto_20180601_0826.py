# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-01 00:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0010_auto_20180531_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
