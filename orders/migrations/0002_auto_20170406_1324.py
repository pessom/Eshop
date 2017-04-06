# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_address',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='productsinorder',
            name='number',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='productsinorder',
            name='price_per_itom',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='productsinorder',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
