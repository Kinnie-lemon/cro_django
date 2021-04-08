from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
'''
先写普通字段，再写外键字段
'''
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
        
class UserInfo(AbstractUser):
    '''

    '''
    phone = models.CharField(null=True, verbose_name='phone',max_length=32,blank=True)
    '''
    null:数据库可以为空
    blank：后台管理可以为空
    '''
    # 头像
    ## 给avatar字段传文件对象 该文件会自动存储到avatar文件下，然后avatar字段只保存文件路径
    name = models.CharField(verbose_name='姓名',max_length=32)
    #account = models.CharField(verbose_name='账号',max_length=32,unique=True)
    is_teacher = models.BooleanField(verbose_name='是否是教职工',default=False)
    avatar = models.FileField(upload_to='avatar/', default='avatar/CROimg.png',verbose_name='用户头像')
    create_time = models.DateField(auto_now_add=True)
    blog = models.OneToOneField(to='Blog',null=True,on_delete=models.CASCADE)
    roles = models.ManyToManyField(verbose_name='拥有的所有角色', to='Role', blank=True)
    def __str__(self):
        return self.username

class Blog(models.Model):
    '''
    个人站点
    '''
    site_name = models.CharField(max_length=32,verbose_name='站点名称')
    site_title = models.CharField(max_length=32,verbose_name='站点标题')
    site_theme = models.CharField(max_length=64,verbose_name='站点样式')
    def __str__(self):
        return self.site_name

class Category(models.Model):
    name = models.CharField(max_length=32,verbose_name='文章分类')
    blog = models.OneToOneField(to='Blog',null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=32,verbose_name='文章标签')
    blog = models.OneToOneField(to='Blog',null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=64,verbose_name='文章标题')
    desc = models.CharField(max_length=255,verbose_name='文章简介')
    content = models.TextField(verbose_name='文章内容')
    create_time = models.DateTimeField(auto_now_add=True)

    ## 字段优化
    up_num = models.BigIntegerField(verbose_name='点赞数',default=0)
    down_num = models.BigIntegerField(verbose_name='点踩数',default=0)
    comment_num = models.BigIntegerField(verbose_name='评论数',default=0)

    ## 外键字段
    blog = models.ForeignKey(to='Blog',null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(to='Category',null=True,on_delete=models.CASCADE)
    tags = models.ManyToManyField(to='Tags',through='Atcl2Tags',
    through_fields=('article','tag'))
    def __str__(self):
        return self.title

class Atcl2Tags(models.Model):
    article = models.ForeignKey(to='Article',on_delete=models.CASCADE)
    tag = models.ForeignKey(to='Tags',on_delete=models.CASCADE)

class upanddown(models.Model):
    user = models.ForeignKey(to='UserInfo',on_delete=models.CASCADE)
    article = models.ForeignKey(to='Article',on_delete=models.CASCADE)
    is_up = models.BooleanField()

class Comment(models.Model):
    user = models.ForeignKey(to='UserInfo', on_delete=models.CASCADE)
    article = models.ForeignKey(to='Article', on_delete=models.CASCADE)
    content = models.CharField(verbose_name='评论内容',max_length=255)
    comment_time = models.DateTimeField(auto_now_add=True)
    ## 根评论自关联
    parent = models.ForeignKey(to='self', null=True, on_delete=models.CASCADE)