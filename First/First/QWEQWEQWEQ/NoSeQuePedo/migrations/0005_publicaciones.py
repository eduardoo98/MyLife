# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NoSeQuePedo', '0004_añadirusuarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=280)),
            ],
        ),
    ]
