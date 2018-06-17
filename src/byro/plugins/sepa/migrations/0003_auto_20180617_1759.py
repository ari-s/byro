# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-17 17:59
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sepa', '0002_auto_20171013_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='membersepa',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(1, 1, 1, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='membersepa',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='membersepa',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='membersepa',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]