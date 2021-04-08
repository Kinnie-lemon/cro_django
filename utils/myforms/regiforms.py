from django import forms
from app02_blog import models

class RegForm(forms.Form):
    username = forms.CharField(label='账号',
                    max_length=32, min_length=2,
                    error_messages={
                        'required':'用户名不能为空',
                        'min_length':'用户名最少2位',
                        'max_length':'用户名最大10位',
                    },
                    widget=forms.widgets.TextInput(attrs={'class':'form-control'}))
    name = forms.CharField(label='姓名',
                    max_length=10, min_length=2,
                    error_messages={
                        'required':'用户名不能为空',
                        'min_length':'用户名最少2位',
                        'max_length':'用户名最大10位',
                    },
                    widget=forms.widgets.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='密码',
    max_length=10, min_length=2,
                    error_messages={
                        'required':'密码不能为空',
                        'min_length':'密码最少2位',
                        'max_length':'密码最大10位',
                    },
                    widget=forms.widgets.TextInput(attrs={'class':'form-control'}))

    confirm_password = forms.CharField(label='确认密码',
    max_length=10, min_length=2,
                    error_messages={
                        'required':'密码不能为空',
                        'min_length':'密码最少2位',
                        'max_length':'密码最大10位',
                    },
                    widget=forms.widgets.TextInput(attrs={'class':'form-control'}))
    
    email = forms.EmailField(label='邮箱',error_messages={
        'invalid':'邮箱格式不正确',
        'required':'邮箱不能为空'},
        widget=forms.widgets.TextInput(attrs={'class':'form-control'}))
    is_teacher = forms.fields.ChoiceField(label='是否内部教职工',choices=((1,'是'),(2,'否')),
                                error_messages={'required':'必须选择用户属性'},
                                widget=forms.widgets.RadioSelect())
    ## 局部钩子：校验用户名是否已存在
    def clean_usernames(self):
        username = self.cleaned_data.get('username')
        ## 在数据库校验
        is_exist = models.UserInfo.objects.filter(username=username)
        if is_exist:
            ## 提示信息
            self.add_error('username','用户名已存在')
        return username
    
    ## 全局钩子
    def clean(self):
        password= self.cleaned_data.get('password')
        confirm_password= self.cleaned_data.get('confirm_password')
        if not password == confirm_password:
            self.add_error('confirm_password','两次密码不一致')
        return self.cleaned_data

        