# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 22:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160609_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('atualizado', models.DateTimeField(auto_now=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Estado')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
    ]
