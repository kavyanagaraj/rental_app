# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 22:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('description', models.TextField(max_length=225)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rented_at_start', models.DateField()),
                ('rented_at_end', models.DateField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_rental', to='add_item.Product')),
                ('renter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_rental', to='login.User')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('product', models.ManyToManyField(related_name='product_tag', to='add_item.Product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='rental',
            field=models.ManyToManyField(through='add_item.Rental', to='login.User'),
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='login.User'),
        ),
    ]
