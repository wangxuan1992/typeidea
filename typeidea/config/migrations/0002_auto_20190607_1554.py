# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-07 07:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='create_time',
            new_name='created_time',
        ),
        migrations.RenameField(
            model_name='sidebar',
            old_name='create_time',
            new_name='created_time',
        ),
    ]
