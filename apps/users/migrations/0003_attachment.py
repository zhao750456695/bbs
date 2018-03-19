# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-18 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180317_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='', upload_to='img')),
                ('file', models.FileField(default='', upload_to='file')),
                ('video', models.FileField(default='', upload_to='video')),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('mtime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]