from django.db import models
import datetime
#from app03_sales.models import Payment,Customer

# Create your models here.
class Students(models.Model):
    stu_name = models.CharField(max_length=32)
    stu_account = models.CharField(max_length=32)
    stu_password = models.CharField(max_length=32) 
    #和学生详情一对一，建在查询频率高的表
    stu_detail = models.OneToOneField(to='Stu_detail',on_delete=models.CASCADE)
    regi_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.stu_name

class Stu_detail(models.Model):
    tel = models.CharField(max_length=32,null=True)##integer可能会超限
    addr = models.CharField(max_length=32,null=True)
    school = models.CharField(max_length=32,null=True)
    birthday = models.DateField()
    class_count = models.IntegerField(verbose_name="已上课时")
    class_remain = models.IntegerField(verbose_name="剩余课时")
    class_left = models.IntegerField(verbose_name="缺课次数")
    class_price = models.IntegerField(verbose_name="课程金额")
    #一对多：models.ForeignKey(to="xxxx")，建在多的一方，to少的一方
    ## 学生和教师多对多，orm外键字段键在任意一方均可，一般在使用频率高的表，不需要再创一张表
    #teacher是虚拟字段，告诉orm创建一个多对多关系
    #teachers = models.ManyToManyField(to='Teachers')
    #classes = models.ManyToManyField(to='Classes')
    #classes_process = models.ManyToManyField(to='Class_bkp')


class Salers(models.Model):
    sale_name = models.CharField(max_length=32,default='cc')
    sale_account = models.CharField(max_length=32,unique=True)
    sale_password = models.CharField(max_length=32)
    if_admin = models.BooleanField(default=False)
    ## 小数总共4位，小数点后2位
    regi_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.sale_name


class Teachers(models.Model):
    tch_name = models.CharField(max_length=32)
    tch_account = models.CharField(max_length=32,unique=True)
    tch_password = models.CharField(max_length=32)
    ## 小数总共4位，小数点后2位
    regi_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.tch_name

class Files(models.Model):
    uploader = models.ForeignKey(to='Teachers',to_field='tch_account',on_delete= models.CASCADE,verbose_name='上传用户',related_name='上传用户')
    ## 给avatar字段传文件对象 该文件会自动存储到avatar文件下，然后avatar字段只保存文件路径
    files = models.FileField(upload_to='files/',verbose_name='上传文件')
    #size = models.CharField(max_length=16)
    cc = models.ForeignKey(to='Teachers',verbose_name='抄送人',to_field='tch_account',on_delete= models.CASCADE,related_name='抄送人',null=True,blank=True)
    verify_person = models.ForeignKey(to='Teachers',to_field='tch_account',verbose_name='审核人',on_delete= models.CASCADE,related_name='审核人',null=True,blank=True)
    if_verify = models.CharField(max_length=10,default='0')
    ## 0：未审核
    verify_mode = models.CharField(max_length=10,default='0')
    notes = models.TextField(blank=True,null=True,verbose_name='文件备注')
    create_time = models.DateField(auto_now_add=True)

class Outline(models.Model):
    cid=models.IntegerField(verbose_name='编号')
    uploader = models.ForeignKey(to='Teachers',to_field='tch_account',on_delete= models.CASCADE,verbose_name='上传用户',related_name='上传教师')
    ## 给avatar字段传文件对象 该文件会自动存储到avatar文件下，然后avatar字段只保存文件路径
    files = models.FileField(upload_to='outline/',verbose_name='上传文件')
    #size = models.CharField(max_length=16)
    category = models.ForeignKey(to='Class_category',on_delete= models.CASCADE,verbose_name='课程分类')
    theme = models.CharField(max_length=32,verbose_name='上课主题')
    description = models.TextField(blank=True,null=True,verbose_name='课程描述')
    notes = models.TextField(blank=True,null=True,verbose_name='文件备注')
    create_time = models.DateField(auto_now_add=True)

class Class_category(models.Model):
    name = models.CharField(max_length=32,verbose_name='课程分类')
    def __str__(self):
        return self.name

class Classes(models.Model):
    cid = models.CharField(max_length=10,verbose_name='课程编号')
    class_name = models.CharField(max_length=32)
    class_category = models.CharField(max_length=32)
    if_end = models.BooleanField(default=False)
    class_count = models.IntegerField(verbose_name="已上课时",default=0)
    def __str__(self):
        return self.class_name

class Classrooms(models.Model):
    classroom_name = models.CharField(max_length=32,default='未分配')
    campus = models.CharField(max_length=32,default='未分配')
    resource = models.CharField(max_length=16,default=None)
    def __str__(self):
        return self.classroom_name
    
class Schedules(models.Model):
    class_name = models.ForeignKey(to='Classes',on_delete= models.CASCADE,verbose_name='班级')
    class_room = models.ForeignKey(to='Classrooms',on_delete= models.CASCADE,verbose_name='教室')
    class_teacher = models.ForeignKey(to='Teachers',on_delete= models.CASCADE)
    classes = models.IntegerField(verbose_name='课时')
    beginning = models.DateTimeField()
    ending = models.DateTimeField()
    notes = models.TextField(verbose_name='备注',blank=True,null=True)
    status = models.BooleanField(verbose_name='已完成',default=False)
    regi_date = models.DateField(auto_now_add=True)

class Transcations(models.Model):
    consultor = models.CharField(max_length=32)


class Class_bkp(models.Model):
    '''
    学生A报B课情况
    '''
    stu_name = models.ForeignKey(to='Stu_detail',on_delete= models.CASCADE)
    classes_name = models.ManyToManyField(to='Classes')
    tches_name =  models.ManyToManyField(to='Teachers')
    if_end = models.BooleanField(default=False)
    #class_count = models.IntegerField(verbose_name="已上课时")
    create_time = models.DateField(auto_now=True)
    '''
    relate_payment = models.ManyToManyField(to='app03_sales.Payment')
    
    class_remain = models.IntegerField(verbose_name="剩余课时")
    class_left = models.IntegerField(verbose_name="缺课次数")
    class_price = models.IntegerField(verbose_name="课程金额")
    '''


class Salary(models.Model):
    tch = models.ForeignKey(to="Teachers", on_delete=models.CASCADE)
    class_price = models.IntegerField(verbose_name="课时费",null=True,blank=True)
    other_price = models.IntegerField(verbose_name="其他收入",null=True,blank=True)
    expenditure = models.IntegerField(verbose_name="支出",null=True,blank=True)
    month = models.DateField(verbose_name="月份")
    create_time = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return datetime.datetime.strftime(self.month,"%Y-%m-%d")
        