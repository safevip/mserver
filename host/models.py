from django.db import models

# Create your models here.


from django.db import models


# Create your models here.


class Host(models.Model):
    hostname = models.CharField(max_length=20, verbose_name='主机名')
    address = models.GenericIPAddressField(verbose_name='地址')

    def __str__(self):
        return self.hostname

    class Meta:
        verbose_name = '主机'
        verbose_name_plural = '主机'
        db_table = 'hm_host'


class User(models.Model):
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=20, verbose_name='密码')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "主机用户"
        verbose_name_plural = "主机用户"
        db_table = "hm_user"
