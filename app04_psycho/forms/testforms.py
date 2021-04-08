from django import forms
from app04_psycho import models
import os

class SCL_Form(forms.Form):
    account = forms.CharField(label='账号',
                    max_length=20, min_length=2,
                    error_messages={
                        'required':'用户名不能为空',
                        'min_length':'用户名最少2位',
                        'max_length':'用户名最大10位',
                    },
                    widget=forms.widgets.TextInput(attrs={'class':'form-control'}))

    #date = forms.DateField(label='测试时间')
    #age = forms.IntegerField()
    num_rounds = forms.IntegerField(label='第几次参加测试')
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
    q3 = forms.fields.ChoiceField(label=text[2],choices=answer,widget=forms.widgets.RadioSelect())
    q4 = forms.fields.ChoiceField(label=text[3],choices=answer,widget=forms.widgets.RadioSelect())
    q5 = forms.fields.ChoiceField(label=text[4],choices=answer,widget=forms.widgets.RadioSelect())
    q6 = forms.fields.ChoiceField(label=text[5],choices=answer,widget=forms.widgets.RadioSelect())
    q7 = forms.fields.ChoiceField(label=text[6],choices=answer,widget=forms.widgets.RadioSelect())
    q8 = forms.fields.ChoiceField(label=text[7],choices=answer,widget=forms.widgets.RadioSelect())
    q9 = forms.fields.ChoiceField(label=text[8],choices=answer,widget=forms.widgets.RadioSelect())
    q10 = forms.fields.ChoiceField(label=text[9],choices=answer,widget=forms.widgets.RadioSelect())
    q11 = forms.fields.ChoiceField(label=text[10],choices=answer,widget=forms.widgets.RadioSelect())
    q12 = forms.fields.ChoiceField(label=text[11],choices=answer,widget=forms.widgets.RadioSelect())
    q13 = forms.fields.ChoiceField(label=text[12],choices=answer,widget=forms.widgets.RadioSelect())
    q14 = forms.fields.ChoiceField(label=text[13],choices=answer,widget=forms.widgets.RadioSelect())
    q15 = forms.fields.ChoiceField(label=text[14],choices=answer,widget=forms.widgets.RadioSelect())
    q16 = forms.fields.ChoiceField(label=text[15],choices=answer,widget=forms.widgets.RadioSelect())
    q17 = forms.fields.ChoiceField(label=text[16],choices=answer,widget=forms.widgets.RadioSelect())
    q18 = forms.fields.ChoiceField(label=text[17],choices=answer,widget=forms.widgets.RadioSelect())
    q19 = forms.fields.ChoiceField(label=text[18],choices=answer,widget=forms.widgets.RadioSelect())
    q20 = forms.fields.ChoiceField(label=text[19],choices=answer,widget=forms.widgets.RadioSelect())
    q21 = forms.fields.ChoiceField(label=text[20],choices=answer,widget=forms.widgets.RadioSelect())
    q22 = forms.fields.ChoiceField(label=text[21],choices=answer,widget=forms.widgets.RadioSelect())
    q23 = forms.fields.ChoiceField(label=text[22],choices=answer,widget=forms.widgets.RadioSelect())
    q24 = forms.fields.ChoiceField(label=text[23],choices=answer,widget=forms.widgets.RadioSelect())
    q25 = forms.fields.ChoiceField(label=text[24],choices=answer,widget=forms.widgets.RadioSelect())
    q26 = forms.fields.ChoiceField(label=text[25],choices=answer,widget=forms.widgets.RadioSelect())
    q27 = forms.fields.ChoiceField(label=text[26],choices=answer,widget=forms.widgets.RadioSelect())
    q28 = forms.fields.ChoiceField(label=text[27],choices=answer,widget=forms.widgets.RadioSelect())
    q29 = forms.fields.ChoiceField(label=text[28],choices=answer,widget=forms.widgets.RadioSelect())
    q30 = forms.fields.ChoiceField(label=text[29],choices=answer,widget=forms.widgets.RadioSelect())
    q31 = forms.fields.ChoiceField(label=text[30],choices=answer,widget=forms.widgets.RadioSelect())
    q32 = forms.fields.ChoiceField(label=text[31],choices=answer,widget=forms.widgets.RadioSelect())
    q33 = forms.fields.ChoiceField(label=text[32],choices=answer,widget=forms.widgets.RadioSelect())
    q34 = forms.fields.ChoiceField(label=text[33],choices=answer,widget=forms.widgets.RadioSelect())
    q35 = forms.fields.ChoiceField(label=text[34],choices=answer,widget=forms.widgets.RadioSelect())
    q36 = forms.fields.ChoiceField(label=text[35],choices=answer,widget=forms.widgets.RadioSelect())
    q37 = forms.fields.ChoiceField(label=text[36],choices=answer,widget=forms.widgets.RadioSelect())
    q38 = forms.fields.ChoiceField(label=text[37],choices=answer,widget=forms.widgets.RadioSelect())
    q39 = forms.fields.ChoiceField(label=text[38],choices=answer,widget=forms.widgets.RadioSelect())
    q40 = forms.fields.ChoiceField(label=text[39],choices=answer,widget=forms.widgets.RadioSelect())
    q41 = forms.fields.ChoiceField(label=text[40],choices=answer,widget=forms.widgets.RadioSelect())
    q42 = forms.fields.ChoiceField(label=text[41],choices=answer,widget=forms.widgets.RadioSelect())
    q43 = forms.fields.ChoiceField(label=text[42],choices=answer,widget=forms.widgets.RadioSelect())
    q44 = forms.fields.ChoiceField(label=text[43],choices=answer,widget=forms.widgets.RadioSelect())
    q45 = forms.fields.ChoiceField(label=text[44],choices=answer,widget=forms.widgets.RadioSelect())
    q46 = forms.fields.ChoiceField(label=text[45],choices=answer,widget=forms.widgets.RadioSelect())
    q47 = forms.fields.ChoiceField(label=text[46],choices=answer,widget=forms.widgets.RadioSelect())
    q48 = forms.fields.ChoiceField(label=text[47],choices=answer,widget=forms.widgets.RadioSelect())
    q49 = forms.fields.ChoiceField(label=text[48],choices=answer,widget=forms.widgets.RadioSelect())
    q50 = forms.fields.ChoiceField(label=text[49],choices=answer,widget=forms.widgets.RadioSelect())
    q51 = forms.fields.ChoiceField(label=text[50],choices=answer,widget=forms.widgets.RadioSelect())
    q52 = forms.fields.ChoiceField(label=text[51],choices=answer,widget=forms.widgets.RadioSelect())
    q53 = forms.fields.ChoiceField(label=text[52],choices=answer,widget=forms.widgets.RadioSelect())
    q54 = forms.fields.ChoiceField(label=text[53],choices=answer,widget=forms.widgets.RadioSelect())
    q55 = forms.fields.ChoiceField(label=text[54],choices=answer,widget=forms.widgets.RadioSelect())
    q56 = forms.fields.ChoiceField(label=text[55],choices=answer,widget=forms.widgets.RadioSelect())
    q57 = forms.fields.ChoiceField(label=text[56],choices=answer,widget=forms.widgets.RadioSelect())
    q58 = forms.fields.ChoiceField(label=text[57],choices=answer,widget=forms.widgets.RadioSelect())
    q59 = forms.fields.ChoiceField(label=text[58],choices=answer,widget=forms.widgets.RadioSelect())
    q60 = forms.fields.ChoiceField(label=text[69],choices=answer,widget=forms.widgets.RadioSelect())
    q61 = forms.fields.ChoiceField(label=text[60],choices=answer,widget=forms.widgets.RadioSelect())
    q62 = forms.fields.ChoiceField(label=text[61],choices=answer,widget=forms.widgets.RadioSelect())
    q63 = forms.fields.ChoiceField(label=text[62],choices=answer,widget=forms.widgets.RadioSelect())
    q64 = forms.fields.ChoiceField(label=text[63],choices=answer,widget=forms.widgets.RadioSelect())
    q65 = forms.fields.ChoiceField(label=text[64],choices=answer,widget=forms.widgets.RadioSelect())
    q66 = forms.fields.ChoiceField(label=text[65],choices=answer,widget=forms.widgets.RadioSelect())
    q67 = forms.fields.ChoiceField(label=text[66],choices=answer,widget=forms.widgets.RadioSelect())
    q68 = forms.fields.ChoiceField(label=text[67],choices=answer,widget=forms.widgets.RadioSelect())
    q69 = forms.fields.ChoiceField(label=text[68],choices=answer,widget=forms.widgets.RadioSelect())
    q70 = forms.fields.ChoiceField(label=text[69],choices=answer,widget=forms.widgets.RadioSelect())
    q71 = forms.fields.ChoiceField(label=text[70],choices=answer,widget=forms.widgets.RadioSelect())
    q72 = forms.fields.ChoiceField(label=text[71],choices=answer,widget=forms.widgets.RadioSelect())
    q73 = forms.fields.ChoiceField(label=text[72],choices=answer,widget=forms.widgets.RadioSelect())
    q74 = forms.fields.ChoiceField(label=text[73],choices=answer,widget=forms.widgets.RadioSelect())
    q75 = forms.fields.ChoiceField(label=text[74],choices=answer,widget=forms.widgets.RadioSelect())
    q76 = forms.fields.ChoiceField(label=text[75],choices=answer,widget=forms.widgets.RadioSelect())
    q77 = forms.fields.ChoiceField(label=text[76],choices=answer,widget=forms.widgets.RadioSelect())
    q78 = forms.fields.ChoiceField(label=text[77],choices=answer,widget=forms.widgets.RadioSelect())
    q79 = forms.fields.ChoiceField(label=text[78],choices=answer,widget=forms.widgets.RadioSelect())
    q80 = forms.fields.ChoiceField(label=text[79],choices=answer,widget=forms.widgets.RadioSelect())
    q81 = forms.fields.ChoiceField(label=text[80],choices=answer,widget=forms.widgets.RadioSelect())
    q82 = forms.fields.ChoiceField(label=text[81],choices=answer,widget=forms.widgets.RadioSelect())
    q83 = forms.fields.ChoiceField(label=text[82],choices=answer,widget=forms.widgets.RadioSelect())
    q84 = forms.fields.ChoiceField(label=text[83],choices=answer,widget=forms.widgets.RadioSelect())
    q85 = forms.fields.ChoiceField(label=text[84],choices=answer,widget=forms.widgets.RadioSelect())
    q86 = forms.fields.ChoiceField(label=text[85],choices=answer,widget=forms.widgets.RadioSelect())
    q87 = forms.fields.ChoiceField(label=text[86],choices=answer,widget=forms.widgets.RadioSelect())
    q88 = forms.fields.ChoiceField(label=text[87],choices=answer,widget=forms.widgets.RadioSelect())
    q89 = forms.fields.ChoiceField(label=text[88],choices=answer,widget=forms.widgets.RadioSelect())
    q90 = forms.fields.ChoiceField(label=text[89],choices=answer,widget=forms.widgets.RadioSelect())


class conners_Form(forms.Form):
    account = forms.CharField(label='账号',
                    max_length=20, min_length=2,
                    error_messages={
                        'required':'用户名不能为空',
                        'min_length':'用户名最少2位',
                        'max_length':'用户名最大10位',
                    },
                    widget=forms.widgets.TextInput(attrs={'class':'form-control'}))

    birth = forms.DateTimeField(label='生日',widget=forms.widgets.DateInput(attrs={'class':'form-control','type':'date'}))
    num_rounds = forms.IntegerField(label='第几次参加测试')
    answer = [[1,'无'],[2,'稍有'],[3,'略多'],[4,'很多']]
    current = os.getcwd()
    txtFileName = 'Conners_teacher.txt'
    txtFolderName = 'app04_psycho/media/psycho'
    txtPathName = '%s/%s/%s'%(current,txtFolderName,txtFileName)

    with open(txtPathName,'r',encoding='utf-8') as f:
        text = []
        for line in f.readlines():
            text.append(line)

    q1 = forms.fields.ChoiceField(label=text[0],choices=answer,widget=forms.widgets.RadioSelect())
    q2 = forms.fields.ChoiceField(label=text[1],choices=answer,widget=forms.widgets.RadioSelect())
    q3 = forms.fields.ChoiceField(label=text[2],choices=answer,widget=forms.widgets.RadioSelect())
    q4 = forms.fields.ChoiceField(label=text[3],choices=answer,widget=forms.widgets.RadioSelect())
    q5 = forms.fields.ChoiceField(label=text[4],choices=answer,widget=forms.widgets.RadioSelect())
    q6 = forms.fields.ChoiceField(label=text[5],choices=answer,widget=forms.widgets.RadioSelect())
    q7 = forms.fields.ChoiceField(label=text[6],choices=answer,widget=forms.widgets.RadioSelect())
    q8 = forms.fields.ChoiceField(label=text[7],choices=answer,widget=forms.widgets.RadioSelect())
    q9 = forms.fields.ChoiceField(label=text[8],choices=answer,widget=forms.widgets.RadioSelect())
    q10 = forms.fields.ChoiceField(label=text[9],choices=answer,widget=forms.widgets.RadioSelect())
    q11 = forms.fields.ChoiceField(label=text[10],choices=answer,widget=forms.widgets.RadioSelect())
    q12 = forms.fields.ChoiceField(label=text[11],choices=answer,widget=forms.widgets.RadioSelect())
    q13 = forms.fields.ChoiceField(label=text[12],choices=answer,widget=forms.widgets.RadioSelect())
    q14 = forms.fields.ChoiceField(label=text[13],choices=answer,widget=forms.widgets.RadioSelect())
    q15 = forms.fields.ChoiceField(label=text[14],choices=answer,widget=forms.widgets.RadioSelect())
    q16 = forms.fields.ChoiceField(label=text[15],choices=answer,widget=forms.widgets.RadioSelect())
    q17 = forms.fields.ChoiceField(label=text[16],choices=answer,widget=forms.widgets.RadioSelect())
    q18 = forms.fields.ChoiceField(label=text[17],choices=answer,widget=forms.widgets.RadioSelect())
    q19 = forms.fields.ChoiceField(label=text[18],choices=answer,widget=forms.widgets.RadioSelect())
    q20 = forms.fields.ChoiceField(label=text[19],choices=answer,widget=forms.widgets.RadioSelect())
    q21 = forms.fields.ChoiceField(label=text[20],choices=answer,widget=forms.widgets.RadioSelect())
    q22 = forms.fields.ChoiceField(label=text[21],choices=answer,widget=forms.widgets.RadioSelect())
    q23 = forms.fields.ChoiceField(label=text[22],choices=answer,widget=forms.widgets.RadioSelect())
    q24 = forms.fields.ChoiceField(label=text[23],choices=answer,widget=forms.widgets.RadioSelect())
    q25 = forms.fields.ChoiceField(label=text[24],choices=answer,widget=forms.widgets.RadioSelect())
    q26 = forms.fields.ChoiceField(label=text[25],choices=answer,widget=forms.widgets.RadioSelect())
    q27 = forms.fields.ChoiceField(label=text[26],choices=answer,widget=forms.widgets.RadioSelect())
    q28 = forms.fields.ChoiceField(label=text[27],choices=answer,widget=forms.widgets.RadioSelect())