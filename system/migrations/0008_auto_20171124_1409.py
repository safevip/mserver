# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 06:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0007_auto_20171123_1328'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permission',
            options={'permissions': (('host_list', '主机列表'), ('host_add', '新增主机'), ('host_del', '删除主机'), ('project_list', '项目列表'), ('project_detail', '项目详情'), ('project_add', '新增项目'), ('project_del', '删除项目'), ('project_edit', '编辑项目'), ('project_task_list', '任务列表'), ('project_task_add', '新增任务'), ('project_task_del', '删除任务'), ('project_task_edit', '编辑任务')), 'verbose_name': '权限表', 'verbose_name_plural': '权限表'},
        ),
    ]