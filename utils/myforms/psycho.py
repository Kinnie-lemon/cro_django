from django import forms
from app04_psycho import models
import os

class Psycho_From(forms.Form):
    username = forms.CharField(label='账号',
                    max_length=10, min_length=2,
                    error_messages={
                        'required':'用户名不能为空',
                        'min_length':'用户名最少2位',
                        'max_length':'用户名最大10位',
                    },
                    widget=forms.widgets.TextInput(attrs={'class':'form-control'}))

    age = forms.IntegerField(label='年龄')
    answer = [[1,'从无'],[2,'很轻'],[3,'中等'],[4,'偏重'],[5,'严重']]
    current = os.getcwd()
    txtFileName = 'SCL_90.txt'
    txtFolderName = 'app04_psycho/media/psycho'
    txtPathName = '%s/%s/%s'%(current,txtFolderName,txtFileName)

    with open(txtPathName,'r',encoding='utf-8') as f:
        text = []
        for line in f.readlines():
            text.append(line)

    q1 = forms.fields.ChoiceField(label=text[0],choices=answer,widget=forms.widgets.RadioSelect())
    q2 = forms.fields.ChoiceField(label=text[1],choices=answer,widget=forms.widgets.RadioSelect())
