# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-11 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IHAM_app', '0003_orderlist_promocode'),
    ]

    operations = [
        migrations.CreateModel(
            name='upcomingEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=140)),
                ('eventURL', models.CharField(max_length=140)),
                ('eventDate', models.CharField(max_length=140)),
                ('eventVenue', models.CharField(max_length=140)),
            ],
        ),
    ]