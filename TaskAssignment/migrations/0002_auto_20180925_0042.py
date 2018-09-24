# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-09-24 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskAssignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Started', 'Started'), ('Completed', 'Completed')], default='Pending', max_length=10),
        ),
    ]
