# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 06:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20171122_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='project.Project', verbose_name='项目'),
        ),
    ]