# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-12 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedor', '0014_auto_20160812_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
