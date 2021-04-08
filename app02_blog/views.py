from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib import auth 
from django.contrib.auth.decorators import login_required
from django.db.models import Count, F
from utils.page_style import Pagination
import datetime
import json
from django.db import transaction
from django.core.mail import send_mail
## 处理年月
from django.db.models.functions import TruncMonth
## 图片处理
from PIL import Image, ImageDraw, ImageFont
import random
'''
Image:生成图片
ImageDraw：在图上画画
ImageFont：控制字体样式
'''
from io import BytesIO, StringIO
'''
内存管理模块
BytesIO：临时存储数据，返回二进制形式
'''
from regiforms import RegForm
from app02_blog import models
from app03_sales import models as md3
from rbac import models as md
from bs4 import BeautifulSoup
import os
from ClassProject import settings
from rbac.service.init_permission import init_permission

# Create your views here.
def register(request):
    form_obj = RegForm()
    if request.method == 'POST':
        ## 校验数据是否合法
        form_obj = RegForm(request.POST)
        back_dic = {'code':1000, 'msg':''}
        ## 判断数据是否合法
        if form_obj.is_valid():
            clean_data = form_obj.cleaned_data
            ## 删除字典中的confirm password
            clean_data.pop('confirm_password')
            ## 获取用户头像
            file_obj = request.FILES.get('avatar')
            ## 判断是否传值，不能直接添加到字典里
            if file_obj:
                clean_data['avatar'] = file_obj
            ## 保存到数据库
            models.UserInfo.objects.create_user(**clean_data)
            back_dic['url'] = '/login/'
        else:
            back_dic['code'] = 2000
            back_dic['msg'] = form_obj.errors
            return JsonResponse(back_dic)
    return render(request,'register.html',locals())

def login(request):
    if request.method == 'POST':
        back_dic ={'code':1000,'msg'
        :''}
        username = request.POST.get('username')
        password = request.POST.get('password')
        code = request.POST.get('code')
        print(request.session.get('code'))
        ## 1. 校验验证码
        if request.session.get('code').upper() == code.upper():
            ## 2.校验用户名和密码
            user_obj = auth.authenticate(request,username=username,password=password)
            if user_obj:
                ## 3.登陆成功，保存用户状态
                auth.login(request,user_obj)
                back_dic['url'] = '/home/'
                
                current_user = md.UserInfo.objects.filter(name=username).first()
                '''
                ## 获取当前用户的权限
                permission_queryset = current_user.roles.filter(permissions__isnull=False).values('permissions__id', 'permissions__url').distinct()
                print(permission_queryset)
                ## 获取权限中所有url
                permission_list = [item['permissions__url'] for item in permission_queryset]
                ## 存入session
                request.session[settings.PERMISSION_SESSION_KEY] = permission_list 
                '''
                init_permission(current_user,request)
            else:
                back_dic['code'] = 2000
                back_dic['msg'] = '用户名或密码错误'
        else:
            back_dic['code'] =3000
            back_dic['msg'] = '验证码错误'
        return JsonResponse(back_dic)
    return render(request,'login.html',locals())


def get_code(request):
    ## 利用pillow模块动态产生图片
    img_obj = Image.new('RGB',(380,35),get_random())
    ## 绘图
    ### 产生一个画笔对象
    img_draw = ImageDraw.Draw(img_obj)
    ### 字体样式 大小
    img_font = ImageFont.truetype('static/fonts/BRITANIC.ttf',38)
    ## 随机验证码
    code =""
    for i in range(5):
        random_upper = chr(random.randint(65,98))
        random_lower = chr(random.randint(97,122))
        random_int = str(random.randint(0,9))
        ## 随机选一个
        tmp =random.choice([random_upper,random_lower,random_int])
        ## 写入图片
        img_draw.text((i*45+60,0), tmp,get_random(),img_font)
        code += tmp
    ## 储存验证码比对时使用
    request.session['code'] = code
    ## 先保存图片
    io_obj = BytesIO() ## 生成一个内存管理器对象
    img_obj.save(io_obj,'png')
    ## 从内存管理其中读取对象返回给前端
    return HttpResponse(io_obj.getvalue())

def get_random():
    return random.randint(0,255),random.randint(0,255),random.randint(0,255)

@login_required
def set_password(request):
    if request.method == 'POST':
        back_dic={'code':1000, 'msg':''}
        if request.is_ajax():
            old_password = request.POST.get('old_password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            is_right =request.user.check_password(old_password)
            if is_right:
                if new_password == confirm_password:
                    request.user.set_password(new_password)
                    request.user.save()
                    back_dic['msg'] = '修改成功'
                else:
                    back_dic['code'] = 1001
                    back_dic['msg'] = '两次密码不一致'
            else:
                back_dic['code'] = 1002
                back_dic['msg'] = '原密码错误'
            return JsonResponse(back_dic)
    return render(request)

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/home/')


def chome(request):
    article_queryset = models.Article.objects.all()
    return render(request,'chome.html',locals())

def site(request,username=None,**kwargs):
    '''
    :param kwargs；如果该参数有值 则需要对article_list做额外操作
    '''
    ## 先校验用户名对应的个人站点是否存在
    user_obj = models.UserInfo.objects.filter(username=username).first()
    ## 用户如果不存在，则返回404页面
    if not user_obj:
        return render(request,'errors.html')
    blog = user_obj.blog
    # 查询当前个人站点下的所有文章
    article_list = models.Article.objects.filter(blog=blog)
    if kwargs:
        condition = kwargs.get('condition')
        param = kwargs.get('param')
        ## 判断用户到底想按照那个条件筛选数据
        if condition == 'category':
            article_list = article_list.filter(category_id=param)
        elif condition == 'tag':
            article_list = article_list.filter(tags=param)
        else:
            year,month = param.split('-')
            article_list = article_list.filter(create_time__year=year, create_time__month=month)
    # 查询当前用户所有的分类，以及分类下的文章（聚合函数）
    category_list = models.Category.objects.filter(blog=blog).annotate(count_num = Count('article__pk')).values('name','count_num','pk')
    # 查询当前用户所有标签及标签下文章数
    tag_list = models.Tags.objects.filter(blog=blog).annotate(count_num = Count('article__pk')).values('name','count_num','pk')
    # 按年月归档
    date_list = models.Article.objects.filter(blog=blog).annotate(month=TruncMonth('create_time')).values('month').annotate(count_num = Count('pk')).values('month','count_num','pk')

    return render(request,'site.html',locals())


def article_detail(request,username, article_id):
    ''' 还需要确认id是否存在
    '''
    ## 1. 获取文章对象
    user_obj = models.UserInfo.objects.filter(username=username).first()
    blog = user_obj.blog
    article_obj = models.Article.objects.filter(pk=article_id,blog__userinfo__username=username).first()
    if not article_obj:
        return render(request,'errors.html')
    ## 2. 获取文章内容
    comment_list = models.Comment.objects.filter(article=article_obj)
    return render(request,'article_detail.html',locals())

def up_and_down(request):
    '''
    Up and down
    1. 校验用户是否登陆
    2. 判断当前文章是否是当前用户，不能给自己点赞
    3. 不能重复点
    4. 操作数据库
    '''
    
    if request.is_ajax():
        back_dic ={'code':1000, 'msg':''}
        ## 1. 判断校验用户是否登录
        if request.user.is_authenticated():
            article_id = request.POST.get('article_id')
            is_up = request.POST.get('is_up')
            is_up = json.loads(is_up)
            ## 2. 不能给自己点赞
            article_obj = models.Article.objects.filter(pk=article_id).first()
            if not article_obj.blog.userinfo == request.user:
                ## 3. 校验是否已点赞
                is_click = models.upanddown.objects.filter(user=request.user,article=article_obj)
                if not is_click:
                    ## 4. 操作数据库 记录数据 同步操作普通字段
                    ## 判断当前用户点了赞还是点了踩
                    
                    if is_up:
                        ## 点赞数+1
                        models.Article.objects.filter(pk=article_id).update(up_num = F('up_num')+1)
                        back_dic['msg'] = '点赞成功'
                    else:
                        models.Article.objects.filter(pk=article_id).update(down_num = F('down_num')+1)
                        back_dic['msg'] = '点踩成功'
                    ## 操作点赞点踩表
                    models.upanddown.objects.create(user=request.user,article=article_obj,is_up=is_up)
                else:
                    back_dic['code'] = 1001
                    back_dic['msg'] = '您已点过，不能再点'
            else:
                back_dic['code'] = 1002
                back_dic['msg'] = '您不能给自己点赞点踩'
        else:
            back_dic['code'] = 1003
            back_dic['msg'] = '请先<a href="/login/">登录</a>'
    return JsonResponse(back_dic)


def comment(request):
    back_dic ={'code':1000, 'msg':''}
    if request.is_ajax():
        
        print(back_dic)
        if request.method == 'POST':
            ## 1. 是否登录
            if request.user.is_authenticated():
                article_id = request.POST.get('article_id')
                content = request.POST.get('content')
                parent_id = request.POST.get('parent_id')
                parent_user = models.UserInfo(pk=parent_id)
                article_obj = models.Article.objects.filter(pk=article_id).first()
                ## 用事务操作表
                with transaction.atomic():
                    models.Article.objects.filter(pk=article_id).update(comment_num = F('comment_num')+1)
                    models.Comment.objects.create(user=request.user,article_id=article_id,content=content,parent_id = parent_id)
                back_dic['msg'] = '评论成功'

                '''
                send_mail(
                    "您的文章%s新增了一条评论内容"%article_obj.title,
                    content,
                    settings.EMAIL_HOST_USER,
                    [""],

                )
                
                ## 设置多线程
                import threading
                threading.Thread(target=send_mail,args=(
                    "您的文章%s新增了一条评论内容"%article_obj.title,
                    content,
                    settings.EMAIL_HOST_USER,
                    [""],
                ))
                '''
            else:
                back_dic['msg'] = '用户未登录'
                back_dic['code'] = 1001
    return JsonResponse(back_dic)


@login_required
def backend(request,username):
    article_list = models.Article.objects.filter(blog=request.user.blog)
    page_obj = Pagination(current_page=request.GET.get('page',1),all_count=article_list.count())
    page_queryset = article_list[page_obj.start:page_obj.end]
    return render(request, 'backend.html',locals())

@login_required
def add_article(request,username):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        tag_id_list = request.POST.getlist('tag')
        ## beautiful soup 抓取内容
        soup = BeautifulSoup(content,'html.parser')
        ### 获取所有标签
        tags = soup.find_all()
        for tag in tags:
            if tag.name == 'script':
                tag.decompose()
        desc = soup.text[0:150]
        models.Article.objects.create(title=title,
        content=str(soup),desc=desc,category_id=category_id,blog=request.user.blog)
        ## 自己创建的第三张表 不能使用add等，可以使用批量插入一次创建多条数据
        article_obj_list=[]
        for i in tag_id_list:
            article_obj_list.append(models.Atcl2Tags(article=article_obk, tag_id=i))
        models.Atcl2Tags.objects.bulk_create(article_obj_list)
        return redirect('/backend/%s'%username)
    category_list = models.Category.objects.filter(blog=request.user.blog)
    tag_list = models.Tags.objects.filter(blog=request.user.blog)
    return render(request,'add_article.html',locals())

def upload_image(request):
    if request.method == 'POST':
        ## 默认成功
        back_dic = {'error':0}
        ## 获取用户上传的图片对象
        file_obj = request.FILES.get('imgFile')
        ## 手动拼接存储路径
        file_dir = os.path.join(settings.BASE_DIR, 'media', 'article_img')
        ## 先判断是否存在文件夹，不存在则自动创建
        if not os.path.isdir(file_dir):
            os.mkdir(file_dir) # 创建一层目录结构
        #file_obj.name = 
        file_path = os.path.join(file_dir,file_obj.name)
        with open(file_path,'wb') as f:
            for line in file_obj:
                f.write(line)
        back_dic['url'] = '/media/article_img/%s'%file_obj.name
    else:
        back_dir['error'] = 1
    return JsonResponse(back_dic)

def set_avatar(request):

    return render(request,'set_avatar.html',locals())


