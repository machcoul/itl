# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20171030_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='oddsname',
            field=models.CharField(max_length=30, null=True),
        ),
    ]