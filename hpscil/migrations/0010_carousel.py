# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hpscil', '0009_remove_teaminfo_qrcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
