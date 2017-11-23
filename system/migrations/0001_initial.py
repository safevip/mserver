# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Right',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='权限名称')),
                ('desc', models.CharField(max_length=50, verbose_name='权限描述')),
                ('url', models.CharField(max_length=100, verbose_name='权限路径')),
                ('parentId', models.IntegerField(verbose_name='父权限id')),
                ('level', models.CharField(max_length=2, verbose_name='权限级别')),
                ('createTime', models.TimeField(verbose_name='创建时间')),
                ('updateTime', models.TimeField(verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '权限',
                'verbose_name_plural': '权限',
                'db_table': 'sys_right',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='角色名称')),
                ('desc', models.CharField(max_length=50, verbose_name='角色描述')),
                ('createTime', models.TimeField(verbose_name='创建时间')),
                ('updateTime', models.TimeField(verbose_name='更新时间')),
                ('creator', models.CharField(max_length=20, verbose_name='创建人')),
                ('updater', models.CharField(max_length=20, verbose_name='修改人')),
                ('rights', models.ManyToManyField(to='system.Right')),
            ],
            options={
                'verbose_name': '角色',
                'verbose_name_plural': '角色',
                'db_table': 'sys_role',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机号')),
                ('createTime', models.TimeField(verbose_name='创建时间')),
                ('updateTime', models.TimeField(verbose_name='更新时间')),
                ('roles', models.ManyToManyField(to='system.Role')),
            ],
            options={
                'verbose_name': '系统用户',
                'verbose_name_plural': '系统用户',
                'db_table': 'sys_user',
            },
        ),
    ]