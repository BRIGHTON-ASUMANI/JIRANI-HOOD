# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-22 18:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='user',
            new_name='admin',
        ),
    ]
