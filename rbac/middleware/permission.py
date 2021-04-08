from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect, HttpResponse
from ClassProject import settings
import re

class CheckPermissionMiddleware(MiddlewareMixin):
    '''
    用户权限校验
    '''
    def process_request(self, request):
        '''
        用户请求进入时触发
        1. 获取当前用户请求的url
        2. 获取当前用户在session中保存的权限列表
        3. 权限信息匹配
        '''
        current_url = request.path_info
        permission_list = request.session.get(settings.PERMISSION_SESSION_KEY)
        valid_url_list = ['/Cshow/login','/home','/get_code','/logout']
        print(permission_list)
        print(current_url)
        ## 访问白名单
        for url in valid_url_list:
            if re.match(url, current_url):
                ## 中间件不拦截
                return None

        if not permission_list:
            return HttpResponse('无权限访问, 请登录')
        flag = False
        for url in permission_list:
            reg = "^%s$" % url
            print(reg)
            if re.match(reg,current_url):
                ## 匹配成功
                flag = True
                break
        if not flag:
            return HttpResponse('您无权限访问')

