# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-20 06:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IHAM_app', '0006_auto_20180118_2252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlist',
            old_name='totalPrice',
            new_name='grandTotalPrice',
        ),
    ]
