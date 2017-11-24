from django.db import models
from host.models import Host

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=20, verbose_name='项目名')
    type = models.CharField(max_length=10, verbose_name='项目类型')
    desc = models.TextField(verbose_name='项目描述')
    path = models.CharField(max_length=100, verbose_name='项目路径')
    package_name = models.CharField(max_length=20, verbose_name='包名')
    on_work = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "pm_project"
        verbose_name = '项目'
        verbose_name_plural = verbose_name


class Task(models.Model):
    name = models.CharField(max_length=20, verbose_name='任务名')
    desc = models.TextField(verbose_name='任务描述')
    type = models.CharField(max_length=10, verbose_name='任务类型')
    script = models.TextField(verbose_name='任务脚本')
    project = models.ForeignKey(Project, verbose_name="项目")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "pm_task"
        verbose_name = '任务'
        verbose_name_plural = verbose_name
