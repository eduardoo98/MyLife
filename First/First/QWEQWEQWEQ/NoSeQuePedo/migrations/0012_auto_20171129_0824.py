# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NoSeQuePedo', '0011_auto_20171129_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='añadirusuarios',
            name='Sexo',
            field=models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='M', max_length=1, null=True),
        ),
    ]
