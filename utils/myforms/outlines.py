#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.forms import ModelForm, Form
from app01 import models


class UploadForm(ModelForm):
    class Meta:
        model = models.Outline ## 对应类
        fields = "__all__"  ## 显示字段
        exclude =["create_time",] ## 排除字段


    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
        self.fields['uploader'].empty_label = "请选择上传人"
        self.fields['description'].strip = False
        self.fields['notes'].strip = False


class UploadUserForm(ModelForm):
    class Meta:
        model = models.Outline
        exclude = ['uploader','create_time']

    def __init__(self, *args, **kwargs):
        super(UploadUserForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

    
