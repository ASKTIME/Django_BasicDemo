# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2021-02-22 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20210222_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hobby',
            field=models.CharField(default='study', max_length=32, verbose_name='爱好'),
        ),
    ]
