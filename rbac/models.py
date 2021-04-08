from django.db import models
#from django.contrib.auth.models import AbstractUser


class Permission(models.Model):
    """
    权限表
    """
    title = models.CharField(verbose_name='标题', max_length=32)
    url = models.CharField(verbose_name='含正则的URL', max_length=128)

    def __str__(self):
        return self.title


class Role(models.Model):
    """
    角色
    """
    title = models.CharField(verbose_name='角色名称', max_length=32)
    permissions = models.ManyToManyField(verbose_name='拥有的所有权限', to='Permission', blank=True)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """
    用户表
    """
    name = models.CharField(verbose_name='用户名', max_length=32,unique=True)
    #account = models.CharField(verbose_name='账号',max_length=20,unique=True)
    is_teacher = models.BooleanField(verbose_name='是否是教职工',default=False)
    password = models.CharField(verbose_name='密码', max_length=64)
    roles = models.ManyToManyField(verbose_name='拥有的所有角色', to='Role', blank=True)
    create_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
