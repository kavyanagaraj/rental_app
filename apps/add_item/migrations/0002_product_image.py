# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=b''),
        ),
    ]
