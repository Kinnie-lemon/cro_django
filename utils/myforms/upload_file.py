from django import forms
from app02_blog import models
from django.forms import fields

class UploadForm(forms.Form):
    uploader = forms.CharField(label='上传人',
                    max_length=100, 
                    error_messages={
                        'not_found':'未找到该用户',
                        'required':'用户名不能为空',
                        'min_length':'用户名最少2位',
                        'max_length':'用户名最大10位',
                    },
                    widget=forms.widgets.TextInput(attrs={'class':'form-control'}))

    #if_verify = forms.ChoiceField(
    #    label="是否需审核",
    #    initial="checked",
    #    widget=forms.widgets.CheckboxInput()
    #)
    cc = forms.CharField(label='抄送人',
                    max_length=100,
                    required=False,
                    error_messages={
                        'not_found':'未找到该用户',
                        'required':'用户名不能为空',
                        'min_length':'用户名最少2位',
                        'max_length':'用户名最大10位',
                    },
                    widget=forms.widgets.TextInput(attrs={'class':'form-control'}))

    verify_person = forms.CharField(label='审核人',
                    max_length=100,required=False,
                    error_messages={
                        'not_found':'未找到该用户',
                        'max_length':'用户名最大10位',
                    },
                    widget=forms.widgets.TextInput(attrs={'class':'form-control'}))

    notes = forms.CharField(label='文件备注',
                            required=False,
                            widget=forms.widgets.TextInput(attrs={'class':'form-control'}))

     ## 全局钩子
    def clean(self):
        
        return self.cleaned_data