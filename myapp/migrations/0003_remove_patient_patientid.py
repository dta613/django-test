# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-24 00:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190324_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='patientid',
        ),
    ]
