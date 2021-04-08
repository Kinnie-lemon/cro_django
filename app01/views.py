from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse,FileResponse
from django.db import connection
import json
from django.core.serializers import serialize
## 链接app01的数据库
from app01 import models
from app03_sales import models as md3
## 分页器
from utils.page_style import Pagination
from upload_file import UploadForm
from outlines import UploadForm,UploadUserForm
import os
from ClassProject import settings
import mimetypes
from django.db.models import Max,Min,Sum,Count,Avg
import re
from django.db.models import F,Q
import datetime
# Create your views here.

def home(request):
    return render(request,'home.html')

def eduadmin(request,class_id):
    '''
    stu_list: 所有学生信息概要
    '''
    ## 在册学生
    ### 查询所有学生信息，传递给html
    
    if class_id == '00':
        stu_list = models.Students.objects.annotate(pay=Sum('payment__money'),
        pays=Count('payment__pk'),sumClass=Sum('payment__purchase_class'),sumGiven=Sum('payment__given_class')).all()
        payment_list = md3.Payment.objects.all()
    else:
        stu_list = models.Students.objects.annotate(pay=Sum('payment__money'),
        pays=Count('payment__pk'),sumClass=Sum('payment__purchase_class'),sumGiven=Sum('payment__given_class')).filter(stu_detail__class_bkp__classes_name__pk=class_id).all()
        payment_list = md3.Payment.objects.filter(stu__stu_detail__class_bkp__classes_name__pk=class_id).all()
    current_page = request.GET.get('page',1)
    all_count = models.Students.objects.count()
    ## 1. 传值实例化
    page_obj = Pagination(current_page=current_page, all_count=all_count)
    ## 2. 直接对总数据进行切片操作
    page_queryset = stu_list[page_obj.start:page_obj.end]
    ## 3. 将page_queryset传递到页面，替换之前的stu_list
    return render(request, 'eduadmin.html',locals())

def eduadmin_class(request):
    '''
    stu_list: 所有学生信息概要
    '''
    ## 在册学生
    ### 查询所有学生信息，传递给html
    stu_list = models.Students.objects.all()
    class_list = models.Classes.objects.annotate(stu_num=Count('class_bkp__pk')).all()
    payment_list = models.Class_bkp.objects.all()
    current_page = request.GET.get('page',1)
    all_count = models.Classes.objects.count()
    ## 1. 传值实例化
    page_obj = Pagination(current_page=current_page, all_count=all_count)
    ## 2. 直接对总数据进行切片操作
    page_queryset = class_list[page_obj.start:page_obj.end]
    ## 3. 将page_queryset传递到页面，替换之前的stu_list
    return render(request, 'eduadmin_class.html',locals())

def stu_add(request):
    ##获取前端提交数据
    if request.method == 'POST':
        stu = request.POST.get("stu_name")
        account = request.POST.get("stu_account")
        password =request.POST.get("password")
        classes = request.POST.getlist("stu_class")
        teachers = request.POST.getlist("stu_teacher")
        tel = request.POST.get('tel')
        addr = request.POST.get('addr')
        birthday = request.POST.get('birthday')
        school = request.POST.get('school')
        ## 存储至数据库
        ### 学员详表
        stu_detail_obj = models.Stu_detail.objects.create(tel=tel, addr=addr, birthday=birthday,school=school)
        ### 详表-class关系表
        stu_detail_obj.classes.add(*classes)
        ### 详表-teahcer关系表
        stu_detail_obj.teachers.add(*teachers)
        ### 学员概述
        stu_obj = models.Students.objects.create(stu_name=stu,stu_account=account,stu_password=password, stu_detail=stu_detail_obj)
        ## 跳转到展示页面
        '''
        可以写url也可以直接写别名
        当别名需要参数时，必须使用reverse解析
        '''
        return redirect('eduadmin')
        
    class_list = models.Classes.objects.all()
    teacher_list = models.Teachers.objects.all()
    return render(request,'stu_add.html', locals())

def stu_edit(request, edit_id):
    edit_obj = models.Students.objects.filter(pk=edit_id).first()
    class_list = models.Classes.objects.all()
    teacher_list = models.Teachers.objects.all()
    ##获取前端提交数据
    if request.method == 'POST':
        stu = request.POST.get("stu_name")
        account = request.POST.get("stu_account")
        password =request.POST.get("password")
        classes = request.POST.getlist("stu_class")
        teachers = request.POST.getlist("stu_teacher")
        tel = request.POST.get('tel')
        addr = request.POST.get('addr')
        birthday = request.POST.get('birthday')
        school = request.POST.get('school')
        ## 存储至数据库
        ### 学员详表
        stu_detail_obj = models.Stu_detail.objects.filter(students__pk=edit_id).first()
        models.Stu_detail.objects.filter(students__pk=edit_id).update(tel=tel, addr=addr, birthday=birthday,school=school)
        ### 详表-class关系表
        class_obj = models.Class_bkp.objects.create(stu_name=stu_detail_obj)
        class_obj.classes_name.set(classes)
        ### 详表-teahcer关系表
        class_obj.tches_name.set(teachers)
        ### 学员概述
        models.Students.objects.filter(pk=edit_id).update(stu_name=stu,stu_account=account,stu_password=password, stu_detail=stu_detail_obj)
        ## 跳转到展示页面
        '''
        可以写url也可以直接写别名
        当别名需要参数时，必须使用reverse解析
        '''
        return redirect('eduadmin')
    ## 获取编辑的对象并展示

    return render(request,'stu_edit.html',locals())

def stu_del(request):
    print('delete')
    if request.is_ajax():
        if request.method == 'POST':
            back_dic = {'code':1000,'msg':''}
            delete_id = request.POST.get("delete_id")
            models.Students.objects.filter(pk=delete_id).delete()
            ## 后端给ajax返回一个字典格式的数据
            back_dic['msg'] = "数据已删除"
            return JsonResponse(back_dic)
    return redirect('eduadmin')


def calendar(request):
    if request.method == 'POST':
        back_dic = {'code':1000,'msg':''}
        class_name = request.POST.get("class_name")
        class_teacher = request.POST.get("class_teacher")
        class_room = request.POST.get("class_room")
        beginning = request.POST.get("beginning")
        ending = request.POST.get("ending")
        notes = request.POST.get("notes")
        print(ending)
        ## 存储至数据库
        ### 日程表
        class_id = models.Classes.objects.filter(class_name=class_name).values("pk")
        class_room_id = models.Classrooms.objects.filter(classroom_name=class_room).values("pk")
        class_teacher_id = models.Teachers.objects.filter(tch_name=class_teacher).values("pk")
        schedule_obj = models.Schedules.objects.create(class_name_id = class_id, class_room_id=class_room_id, 
                                                class_teacher_id = class_teacher_id,
                                                beginning=beginning,ending=ending,notes=notes)
        return JsonResponse(back_dic)
        ## 跳转到展示页面
    class_list = models.Classes.objects.all()
    teacher_list = models.Teachers.objects.all()
    classroom_list = models.Classrooms.objects.all()
    return render(request,'calendar.html',locals())

def get_calendar(request):
    schedule_obj = models.Schedules.objects.all().values('pk','class_name__class_name','class_room__classroom_name','class_room__resource','class_teacher__tch_name','beginning','ending','notes','status')
    json_obj = list(schedule_obj)
    resource_obj = models.Classrooms.objects.all()
    json_resource = json.loads(serialize('json',resource_obj))
    back_dic = {'code':1000,'msg':'','obj':json_obj,'resource':json_resource}
    return JsonResponse(back_dic)


def calendar_del_event(request):
    if request.is_ajax():
        if request.method == 'POST':
            back_dic = {'code':1000,'msg':'传输成功，未删除'}
            delete_id = request.POST.get("delete_id")
            models.Schedules.objects.filter(pk=delete_id).delete()
            back_dic['msg'] = '删除成功'
    return JsonResponse(back_dic)


def save(request):
    form_obj = UploadForm()
    teacher_list = models.Teachers.objects.all()
    data_list = models.Files.objects.all()
    if request.method == 'POST':
        ## 校验数据是否合法
        form_obj = UploadForm(request.POST)
        back_dic = {'code':1000, 'msg':''}
        ## 判断数据是否合法
        if form_obj.is_valid():
            clean_data = form_obj.cleaned_data
            ## 获取文件
            file_obj = request.FILES.get('file_upload')
            if_verify = request.POST.get('if_verify')
            if not if_verify:
                if_verify = '0'
            uploader = request.POST.get('uploader')
            cc = request.POST.get('cc')
            verify_person = request.POST.get('verify_person')
            notes = request.POST.get('notes')
            ## 手动拼接存储路径
            file_dir = os.path.join(settings.BASE_DIR, 'media', 'files')
            ## 判断是否传值，不能直接添加到字典里
            if file_obj:
                clean_data['files'] = file_obj
                clean_data['if_verify'] =if_verify
                ## 先判断是否存在文件夹，不存在则自动创建
                if not os.path.isdir(file_dir):
                    os.mkdir(file_dir) # 创建一层目录结构
                #file_obj.name = 
                file_path = os.path.join(file_dir,file_obj.name)
                with open(file_path,'wb') as f:
                    for line in file_obj:
                        f.write(line)
            #back_dic['url'] = '/media/files/%s'%file_obj.name
            
            ## 保存到数据库
            print(clean_data)
            files_obj = models.Files.objects.create(uploader_id=uploader,cc_id=cc,verify_person_id=verify_person,files=file_obj,if_verify=if_verify,notes=notes)
            
            
            back_dic['url'] = '/save/'
        else:
            back_dic['code'] = 2000
            back_dic['msg'] = form_obj.errors
            return JsonResponse(back_dic)
    return  render(request,'save.html',locals())

def cloud_download(request,file_pk):
    #file_pk = request.GET['file_pk']
    filename = models.Files.objects.filter(pk=file_pk).values('files').first()
    filename = filename.get('files').split('/')[-1]
    file_path = os.path.join(settings.BASE_DIR, 'media','files',filename)
    content_type = mimetypes.guess_type(file_path)[0]
    ext = os.path.basename(file_path).split('.')[-1].lower()
    # cannot be used to download py, db and sqlite3 files.
    if ext not in ['py', 'db',  'sqlite3']:
        file = open(file_path, 'rb')    
        response = FileResponse(file,filename=filename)
        response['Content-Type'] = content_type
        response['Content-Disposition'] = 'attachment;filename=%s' % filename
    return  response 


def eduadmin_class_done(request):
    if request.is_ajax():
        if request.method == 'POST':
            back_dic = {'code':1000,'msg':''}
            done_id = request.POST.get('done_id')
            print(done_id)
            models.Classes.objects.filter(pk=done_id).update(if_end=True)
            back_dic['msg'] = '已结课'
        else:
            back_dic = {'code':2000,'msg':'操作失败'}
        return JsonResponse(back_dic)
    return redirect('eduadmin_class')

def eduadmin_class_del(request):
    print('delete')
    if request.is_ajax():
        if request.method == 'POST':
            back_dic = {'code':1000,'msg':''}
            delete_id = request.POST.get("delete_id")
            models.Classes.objects.filter(pk=delete_id).delete()
            ## 后端给ajax返回一个字典格式的数据
            back_dic['msg'] = "数据已删除"
        else:
                back_dic = {'code':2000,'msg':'操作失败'}
        return JsonResponse(back_dic)
    return redirect('eduadmin')


def eduadmin_roll_list(request,roll_id):
    back_dic = {'code':1000,'msg':''}
    if request.is_ajax():
        roll_obj = models.Classes.objects.filter(pk=roll_id).values("class_bkp__stu_detail__students__stu_name","class_bkp__stu_detail__students__stu_account","class_bkp__pk")
        roll_json = list(roll_obj)
        back_dic['msg'] = '成功'
        back_dic['roll_obj'] = roll_json
    else:
        back_dic = {'code':2000,'msg':'ajax验证错误'}
    #print(back_dic)    
    return JsonResponse(back_dic)

def eduadmin_class_filter(request,filter_mode):
    if filter_mode == 'done':
        class_list = models.Classes.objects.filter(if_end=True).annotate(stu_num=Count('class_bkp__pk')).all()
    elif filter_mode == 'doing':
        class_list = models.Classes.objects.filter(if_end =False).annotate(stu_num=Count('class_bkp__pk')).all()
    elif filter_mode == 'none':
        class_list = models.Classes.objects.filter(class_count=0).annotate(stu_num=Count('class_bkp__pk')).all()

    all_count = models.Class_bkp.objects.count()
    current_page = request.GET.get('page',1)
    ## 1. 传值实例化
    page_obj = Pagination(current_page=current_page, all_count=all_count)
    ## 2. 直接对总数据进行切片操作
    page_queryset = class_list[page_obj.start:page_obj.end]
    ## 3. 将page_queryset传递到页面，替换之前的stu_list
    return render(request, 'eduadmin_class.html',locals())

def eduadmin_class_roll(request):
    if request.is_ajax():
        if request.method == 'POST':
            back_dic = {'code':1000,'msg':''}
            checked_list = request.POST.get("checked_list")
            checked_list = re.sub(r"\"*","",checked_list[1:-1]).split(",")
            if checked_list[0]:
                switch = {
                    "C1" : 1, "C2" : 1, "C3" : 1,
                    "R1":1.5,
                    "R3" : 2, "R5" : 2, "R7" : 2,
                    "P" : 2,
                }
                for i in checked_list:
                    val = models.Class_bkp.objects.filter(pk=i).values("stu_name__pk","stu_name__class_count","stu_name__class_remain","stu_name__classes_name__cid").first()
                    print(val)
                    sid = val.get("stu_name__pk")
                    cid = val.get("classes_name__cid")
                    class_count = val.get("class_count") + switch[cid]
                    class_remain = val.get("class_remain") - switch[cid]
                    models.Stu_detail.objects.filter(pk=sid).update(class_count=class_count,class_remain=class_remain)
                ## 后端给ajax返回一个字典格式的数据
                back_dic['msg'] = "已签到"
            else:
                back_dic = {'code':1001,'msg':'没有选择学员'}
        else:
                back_dic = {'code':2000,'msg':'操作失败'}
        return JsonResponse(back_dic)
    return redirect('eduadmin')

def tch_outline(request,file_pk):
    '''
    查看相应大纲
    '''
    if request.method == 'GET':
        form = UploadForm()
        data = models.Outline.objects.filter(category__pk=file_pk).order_by('cid')
        current_page = request.GET.get('page',1)
        all_count = data.count()
        ## 1. 传值实例化
        page_obj = Pagination(current_page=current_page, all_count=all_count)
        ## 2. 直接对总数据进行切片操作
        page_queryset = data[page_obj.start:page_obj.end]
        return render(request,'outline_base.html',locals())
    print(request.FILES.get('files'))
    form = UploadForm(request.POST,request.FILES)

    if form.is_valid():
        form.save()
        return redirect('/tch/outline/add/')
    return render(request,'outline_base.html',locals())

def add_outline(request):
    """
    新增大纲
    :return:
    """
    if request.method == 'GET':
        form = UploadForm()
        return render(request, 'outline_add.html', {'form': form})
    form = UploadForm(data=request.POST)
    if form.is_valid():
        
            
        form.save()
        return redirect('/tch/outline/add/')
    return render(request, 'outline_add.html', {'form': form})
def sales_warning(request,type):
    '''
    stu_list: 所有学生信息概要
    '''
    ## 在册学生
    ### 查询所有学生信息，传递给html
    stu_list = models.Students.objects.all()
    if type == 'A':##教务
        payment_list = md3.Payment.objects.filter(stu__stu_detail__class_remain__lt=6).all()
    elif type == 'S':##销售
        payment_list = md3.Payment.objects.annotate(pays=Count('stu__pk')).filter(Q(stu__stu_detail__class_bkp__if_end=False) and 
        (
            (Q(pays__lt=2)&(Q(signup_category__name ='季卡') |Q(signup_category__name ='半年卡')))
            |(Q(signup_category__name ='寒假班') |Q(signup_category__name ='暑假班')|Q(signup_category__name ='大卡课')|Q(signup_category__name ='小卡课')))).all()
    elif type == 'F':
        payment_list = md3.Payment.objects.annotate(pays=Count('stu__pk')).filter(Q(stu__stu_detail__class_remain__lt=6)|(Q(stu__stu_detail__class_bkp__if_end=False) and 
        (
            (Q(pays__lt=2)&(Q(signup_category__name ='季卡') |Q(signup_category__name ='半年卡')))
            |(Q(signup_category__name ='寒假班') |Q(signup_category__name ='暑假班')|Q(signup_category__name ='大卡课')|Q(signup_category__name ='小卡课'))))).all()
    admin_count = md3.Payment.objects.filter(stu__stu_detail__class_remain__lt=6).count()
    sale_count = md3.Payment.objects.annotate(pays=Count('stu__pk')).filter(Q(stu__stu_detail__class_bkp__if_end=False) and 
        (
            (Q(pays__lt=2)&(Q(signup_category__name ='季卡') |Q(signup_category__name ='半年卡')))
            |(Q(signup_category__name ='寒假班') |Q(signup_category__name ='暑假班')|Q(signup_category__name ='大卡课')|Q(signup_category__name ='小卡课')))).count()
    current_page = request.GET.get('page',1)
    all_count = payment_list.count()
    ## 1. 传值实例化
    page_obj = Pagination(current_page=current_page, all_count=all_count)
    ## 2. 直接对总数据进行切片操作
    page_queryset = stu_list[page_obj.start:page_obj.end]
    ## 3. 将page_queryset传递到页面，替换之前的stu_list
    return render(request, 'renewal_warning.html',locals())


def data_home(request,account):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    current = datetime.datetime.strptime("{year}-{month}".format(year=year,month=month),"%Y-%m")
    salaries = models.Salary.objects.filter(tch__tch_account=account).all()
    ## 总排课数
    classes_all = models.Teachers.objects.filter(tch_account=account,schedules__ending__gte=current,schedules__status=True).annotate(cls_count=Count('schedules__pk'),cls_sum = Sum('schedules__classes'))
    classes_out = models.Schedules.objects.filter(class_teacher__tch_account=account,ending__gte=current,status=True,class_name__class_category='校外课').count()
    classes_demo = models.Schedules.objects.filter(class_teacher__tch_account=account,ending__gte=current,status=True,class_name__class_category='试听课').count()
    classes_member = models.Schedules.objects.filter(class_teacher__tch_account=account,ending__gte=current,status=True).exclude(Q(class_name__class_category='试听课')|Q(class_name__class_category='校外课')).count()
    warning = models.Teachers.objects.filter(tch_account=account,class_bkp__stu_name__class_remain__lt=6).annotate(stu_count=Count('class_bkp__stu_name__pk'))
    print(classes_all)
    print(classes_out)
    print(classes_demo)
    print(classes_member)
    print(salaries)
    print(warning)
    return render(request,'data_home.html',locals())


