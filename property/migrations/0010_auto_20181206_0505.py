# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-12-06 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20181206_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='postal_code',
            field=models.CharField(max_length=5, unique=True, verbose_name='کد پستی'),
        ),
    ]