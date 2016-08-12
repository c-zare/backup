# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-11 14:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0008_auto_20160811_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]