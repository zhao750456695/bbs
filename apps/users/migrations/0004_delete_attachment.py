# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-18 13:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_attachment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='attachment',
        ),
    ]
