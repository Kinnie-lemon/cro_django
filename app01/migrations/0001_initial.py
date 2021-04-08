# Generated by Django 3.1.6 on 2021-04-06 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='课程分类')),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=10, verbose_name='课程编号')),
                ('class_name', models.CharField(max_length=32)),
                ('class_category', models.CharField(max_length=32)),
                ('if_end', models.BooleanField(default=False)),
                ('class_count', models.IntegerField(default=0, verbose_name='已上课时')),
            ],
        ),
        migrations.CreateModel(
            name='Classrooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_name', models.CharField(default='未分配', max_length=32)),
                ('campus', models.CharField(default='未分配', max_length=32)),
                ('resource', models.CharField(default=None, max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Salers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_name', models.CharField(default='cc', max_length=32)),
                ('sale_account', models.CharField(max_length=32, unique=True)),
                ('sale_password', models.CharField(max_length=32)),
                ('if_admin', models.BooleanField(default=False)),
                ('regi_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stu_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(max_length=32, null=True)),
                ('addr', models.CharField(max_length=32, null=True)),
                ('school', models.CharField(max_length=32, null=True)),
                ('birthday', models.DateField()),
                ('class_count', models.IntegerField(verbose_name='已上课时')),
                ('class_remain', models.IntegerField(verbose_name='剩余课时')),
                ('class_left', models.IntegerField(verbose_name='缺课次数')),
                ('class_price', models.IntegerField(verbose_name='课程金额')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tch_name', models.CharField(max_length=32)),
                ('tch_account', models.CharField(max_length=32, unique=True)),
                ('tch_password', models.CharField(max_length=32)),
                ('regi_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transcations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultor', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=32)),
                ('stu_account', models.CharField(max_length=32)),
                ('stu_password', models.CharField(max_length=32)),
                ('regi_date', models.DateField(auto_now_add=True)),
                ('stu_detail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app01.stu_detail')),
            ],
        ),
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.IntegerField(verbose_name='课时')),
                ('beginning', models.DateTimeField()),
                ('ending', models.DateTimeField()),
                ('notes', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('status', models.BooleanField(default=False, verbose_name='已完成')),
                ('regi_date', models.DateField(auto_now_add=True)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.classes', verbose_name='班级')),
                ('class_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.classrooms', verbose_name='教室')),
                ('class_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.teachers')),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_price', models.IntegerField(blank=True, null=True, verbose_name='课时费')),
                ('other_price', models.IntegerField(blank=True, null=True, verbose_name='其他收入')),
                ('expenditure', models.IntegerField(blank=True, null=True, verbose_name='支出')),
                ('month', models.DateField(verbose_name='月份')),
                ('create_time', models.DateField(auto_now_add=True)),
                ('tch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.teachers')),
            ],
        ),
        migrations.CreateModel(
            name='Outline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField(verbose_name='编号')),
                ('files', models.FileField(upload_to='outline/', verbose_name='上传文件')),
                ('theme', models.CharField(max_length=32, verbose_name='上课主题')),
                ('description', models.TextField(blank=True, null=True, verbose_name='课程描述')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='文件备注')),
                ('create_time', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.class_category', verbose_name='课程分类')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='上传教师', to='app01.teachers', to_field='tch_account', verbose_name='上传用户')),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to='files/', verbose_name='上传文件')),
                ('if_verify', models.CharField(default='0', max_length=10)),
                ('verify_mode', models.CharField(default='0', max_length=10)),
                ('notes', models.TextField(blank=True, null=True, verbose_name='文件备注')),
                ('create_time', models.DateField(auto_now_add=True)),
                ('cc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='抄送人', to='app01.teachers', to_field='tch_account', verbose_name='抄送人')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='上传用户', to='app01.teachers', to_field='tch_account', verbose_name='上传用户')),
                ('verify_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='审核人', to='app01.teachers', to_field='tch_account', verbose_name='审核人')),
            ],
        ),
        migrations.CreateModel(
            name='Class_bkp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('if_end', models.BooleanField(default=False)),
                ('create_time', models.DateField(auto_now=True)),
                ('classes_name', models.ManyToManyField(to='app01.Classes')),
                ('stu_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.stu_detail')),
                ('tches_name', models.ManyToManyField(to='app01.Teachers')),
            ],
        ),
    ]
