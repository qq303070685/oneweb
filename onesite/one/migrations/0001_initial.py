# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-30 02:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('customer_name', models.CharField(max_length=255)),
                ('dfe_name', models.CharField(choices=[('1', 'Pro'), ('2', 'Esko'), ('3', 'PM'), ('4', '\u65e0')], default='2', max_length=255)),
                ('question', models.CharField(max_length=255, unique=True, verbose_name='\u95ee\u9898\u63cf\u8ff0')),
                ('solution', models.TextField()),
                ('solution_or_not', models.BooleanField(default=True)),
                ('update_or_not', models.BooleanField(default=True)),
                ('change_or_not', models.IntegerField(choices=[(1, '\u65e0'), (2, '\u5e93\u623f\u7533\u8bf7'), (3, '\u5c0f\u5e93\u7533\u8bf7'), (4, 'HP\u63d0\u4f9b'), (5, '\u7b2c\u4e09\u65b9\u8d2d\u4e70')], default=1)),
                ('share_or_not', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
