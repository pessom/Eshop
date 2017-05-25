# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-22 08:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_offer_attributes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='attributes',
        ),
        migrations.RemoveField(
            model_name='productclass',
            name='variant_attributes',
        ),
        migrations.AddField(
            model_name='offer',
            name='attribute',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='products.ProductAttribute'),
        ),
    ]