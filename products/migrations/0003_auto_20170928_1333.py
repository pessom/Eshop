# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-28 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20170927_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producer',
            name='image',
            field=models.ImageField(blank=True, upload_to='producers', verbose_name='image of producer'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='image',
            field=models.ImageField(blank=True, upload_to='categories', verbose_name='image of category'),
        ),
    ]