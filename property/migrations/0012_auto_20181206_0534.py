# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-12-06 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20181206_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postalcode',
            name='postalcode',
            field=models.CharField(default='', max_length=5, verbose_name='کدپستی'),
        ),
    ]
