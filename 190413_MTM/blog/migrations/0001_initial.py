# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-12 08:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField(default='')),
                ('author', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
