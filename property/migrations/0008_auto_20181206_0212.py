# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-12-05 22:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20181206_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='postal_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.PostalCode'),
        ),
    ]
