# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-29 01:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0002_auto_20170529_0100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='mode',
            new_name='status',
        ),
    ]