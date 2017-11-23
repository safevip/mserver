from django.db import models
from django.contrib.auth.models import ContentType

# Create your models here.


class Permission(models.Model):
    chioces = ((1, 'GET'), (2, 'POST'))

    describe = models.CharField(max_length=255, verbose_name='权限描述')
    codename = models.CharField(max_length=64, verbose_name="权限码")
    url = models.CharField(max_length=255, verbose_name='URL路径')
    content_type = models.ForeignKey(
        ContentType,
        models.CASCADE,
        related_name='+',
        verbose_name='content type',
        default='',
    )
    per_method = models.SmallIntegerField(choices=chioces, verbose_name='请求方法', default=1)

    def __str__(self):
        return self.describe

    class Meta:
        verbose_name = '权限表'
        verbose_name_plural = verbose_name
        # 所有权限的元组（codename,描述），描述信息是在django admin中显示权限用的
        permissions = (
            ('host_list', '主机列表'),
            ('host_add', '新增主机'),
            ('host_del', '删除主机'),
            ('project_list', '项目列表'),
            ('project_detail', '项目详情'),
            ('project_add', '新增项目'),
            ('project_del', '删除项目'),
            ('project_edit', '编辑项目'),
            ('project_task_list', '任务列表'),
            ('project_task_add', '新增任务'),
            ('project_task_del', '删除任务'),
            ('project_task_edit', '编辑任务'),
        )
        db_table = 'sys_perm'
