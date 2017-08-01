# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-04 18:11
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='28e5f199-85eb-40f8-8e58-66dc91eb9ece', max_length=50, unique=True)),
                ('valid_from', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('valid_to', models.DateTimeField(blank=True, default=datetime.datetime(2017, 7, 11, 18, 11, 37, 603452))),
                ('discount', models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
