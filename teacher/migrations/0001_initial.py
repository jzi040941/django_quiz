# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 12:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('assignNum', models.AutoField(primary_key=True, serialize=False)),
                ('assignName', models.CharField(max_length=30)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subjectNum', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('subjectName', models.CharField(max_length=128)),
                ('classroom', models.CharField(max_length=128)),
                ('classtime', models.DateTimeField()),
                ('professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='subjectNum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Subject'),
        ),
    ]
