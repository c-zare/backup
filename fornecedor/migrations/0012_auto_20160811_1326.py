# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-11 16:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedor', '0011_fornecedor_bairro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Municipio'),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Estado'),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
