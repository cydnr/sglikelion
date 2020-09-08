# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-13 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_follow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=30, null=True)),
                ('follow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Follow')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
    ]
