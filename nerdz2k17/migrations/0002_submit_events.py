# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-14 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nerdz2k17', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submit',
            name='events',
            field=models.CharField(max_length=500, null=True),
        ),
    ]