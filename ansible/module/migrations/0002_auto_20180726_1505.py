# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-26 09:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sample',
            old_name='name',
            new_name='names',
        ),
    ]
