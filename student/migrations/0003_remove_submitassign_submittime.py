# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 12:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20170804_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submitassign',
            name='submittime',
        ),
    ]
