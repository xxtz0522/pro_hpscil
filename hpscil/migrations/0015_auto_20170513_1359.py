# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 05:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hpscil', '0014_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='content',
            field=models.TextField(default='', verbose_name='\u5185\u5bb9'),
        ),
        migrations.AddField(
            model_name='activity',
            name='people_num',
            field=models.IntegerField(default=0, verbose_name='\u4eba\u6570'),
        ),
        migrations.AddField(
            model_name='activity',
            name='place',
            field=models.CharField(default=django.utils.timezone.now, max_length=150, verbose_name='\u5730\u70b9'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='time',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='\u65f6\u95f4'),
        ),
    ]
