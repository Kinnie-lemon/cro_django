# Generated by Django 3.1.6 on 2021-04-06 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=20, verbose_name='账号')),
                ('test', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SCL_90',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_date', models.DateTimeField(auto_now=True)),
                ('age', models.DecimalField(decimal_places=2, max_digits=5)),
                ('num_rounds', models.IntegerField()),
                ('q1', models.IntegerField()),
                ('q2', models.IntegerField()),
                ('q3', models.IntegerField()),
                ('q4', models.IntegerField()),
                ('q5', models.IntegerField()),
                ('q6', models.IntegerField()),
                ('q7', models.IntegerField()),
                ('q8', models.IntegerField()),
                ('q9', models.IntegerField()),
                ('q10', models.IntegerField()),
                ('q11', models.IntegerField()),
                ('q12', models.IntegerField()),
                ('q13', models.IntegerField()),
                ('q14', models.IntegerField()),
                ('q15', models.IntegerField()),
                ('q16', models.IntegerField()),
                ('q17', models.IntegerField()),
                ('q18', models.IntegerField()),
                ('q19', models.IntegerField()),
                ('q20', models.IntegerField()),
                ('q21', models.IntegerField()),
                ('q22', models.IntegerField()),
                ('q23', models.IntegerField()),
                ('q24', models.IntegerField()),
                ('q25', models.IntegerField()),
                ('q26', models.IntegerField()),
                ('q27', models.IntegerField()),
                ('q28', models.IntegerField()),
                ('q29', models.IntegerField()),
                ('q30', models.IntegerField()),
                ('q31', models.IntegerField()),
                ('q32', models.IntegerField()),
                ('q33', models.IntegerField()),
                ('q34', models.IntegerField()),
                ('q35', models.IntegerField()),
                ('q36', models.IntegerField()),
                ('q37', models.IntegerField()),
                ('q38', models.IntegerField()),
                ('q39', models.IntegerField()),
                ('q40', models.IntegerField()),
                ('q41', models.IntegerField()),
                ('q42', models.IntegerField()),
                ('q43', models.IntegerField()),
                ('q44', models.IntegerField()),
                ('q45', models.IntegerField()),
                ('q46', models.IntegerField()),
                ('q47', models.IntegerField()),
                ('q48', models.IntegerField()),
                ('q49', models.IntegerField()),
                ('q50', models.IntegerField()),
                ('q51', models.IntegerField()),
                ('q52', models.IntegerField()),
                ('q53', models.IntegerField()),
                ('q54', models.IntegerField()),
                ('q55', models.IntegerField()),
                ('q56', models.IntegerField()),
                ('q57', models.IntegerField()),
                ('q58', models.IntegerField()),
                ('q59', models.IntegerField()),
                ('q60', models.IntegerField()),
                ('q61', models.IntegerField()),
                ('q62', models.IntegerField()),
                ('q63', models.IntegerField()),
                ('q64', models.IntegerField()),
                ('q65', models.IntegerField()),
                ('q66', models.IntegerField()),
                ('q67', models.IntegerField()),
                ('q68', models.IntegerField()),
                ('q69', models.IntegerField()),
                ('q70', models.IntegerField()),
                ('q71', models.IntegerField()),
                ('q72', models.IntegerField()),
                ('q73', models.IntegerField()),
                ('q74', models.IntegerField()),
                ('q75', models.IntegerField()),
                ('q76', models.IntegerField()),
                ('q77', models.IntegerField()),
                ('q78', models.IntegerField()),
                ('q79', models.IntegerField()),
                ('q80', models.IntegerField()),
                ('q81', models.IntegerField()),
                ('q82', models.IntegerField()),
                ('q83', models.IntegerField()),
                ('q84', models.IntegerField()),
                ('q85', models.IntegerField()),
                ('q86', models.IntegerField()),
                ('q87', models.IntegerField()),
                ('q88', models.IntegerField()),
                ('q89', models.IntegerField()),
                ('q90', models.IntegerField()),
                ('scl_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app04_psycho.info')),
            ],
        ),
        migrations.CreateModel(
            name='conners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_date', models.DateTimeField(auto_now=True)),
                ('age', models.DecimalField(decimal_places=2, max_digits=5)),
                ('num_rounds', models.IntegerField()),
                ('q1', models.IntegerField()),
                ('q2', models.IntegerField()),
                ('q3', models.IntegerField()),
                ('q4', models.IntegerField()),
                ('q5', models.IntegerField()),
                ('q6', models.IntegerField()),
                ('q7', models.IntegerField()),
                ('q8', models.IntegerField()),
                ('q9', models.IntegerField()),
                ('q10', models.IntegerField()),
                ('q11', models.IntegerField()),
                ('q12', models.IntegerField()),
                ('q13', models.IntegerField()),
                ('q14', models.IntegerField()),
                ('q15', models.IntegerField()),
                ('q16', models.IntegerField()),
                ('q17', models.IntegerField()),
                ('q18', models.IntegerField()),
                ('q19', models.IntegerField()),
                ('q20', models.IntegerField()),
                ('q21', models.IntegerField()),
                ('q22', models.IntegerField()),
                ('q23', models.IntegerField()),
                ('q24', models.IntegerField()),
                ('q25', models.IntegerField()),
                ('q26', models.IntegerField()),
                ('q27', models.IntegerField()),
                ('q28', models.IntegerField()),
                ('morality', models.IntegerField()),
                ('activity', models.IntegerField()),
                ('passive', models.IntegerField()),
                ('adhd', models.IntegerField()),
                ('conn_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app04_psycho.info')),
            ],
        ),
    ]