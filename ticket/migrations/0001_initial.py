# Generated by Django 2.1.1 on 2018-09-19 10:21

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('job_title', models.CharField(max_length=32, verbose_name='职位')),
                ('department', models.CharField(max_length=32, verbose_name='部门')),
                ('phone', models.IntegerField(null=True, verbose_name='手机号码')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False, verbose_name='项目编号')),
                ('pname', models.CharField(max_length=200, verbose_name='项目名称')),
                ('pstage', models.CharField(max_length=32, verbose_name='项目阶段')),
                ('pcity', models.CharField(max_length=32, verbose_name='城市')),
                ('poperator', models.CharField(max_length=32, verbose_name='运维')),
                ('pdeveloper', models.CharField(max_length=32, verbose_name='开发')),
                ('psales', models.CharField(max_length=32, verbose_name='销售')),
                ('pmanager', models.CharField(max_length=32, verbose_name='项目经理')),
                ('pbusiness', models.CharField(max_length=32, verbose_name='业务')),
                ('pagent', models.CharField(max_length=64, null=True, verbose_name='代理商')),
                ('pimplementer', models.CharField(max_length=64, verbose_name='实施方')),
                ('pstatus', models.CharField(max_length=64, verbose_name='项目状态')),
                ('pprogress', models.TextField(verbose_name='项目进展')),
                ('pstart_time', models.DateField(verbose_name='开始时间')),
                ('ponline_time', models.DateField(null=True, verbose_name='上线时间')),
                ('pacceptance_time', models.DateField(null=True, verbose_name='验收时间')),
                ('plicense_time', models.CharField(max_length=32, verbose_name='授权时长')),
                ('plicexpire_time', models.DateField(verbose_name='授权到期时间')),
                ('pexpire_time', models.DateField(null=True, verbose_name='维保到期时间')),
                ('psup_type', models.CharField(max_length=32, verbose_name='支持方式')),
            ],
            options={
                'verbose_name': '项目',
                'verbose_name_plural': '项目',
            },
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('tname', models.CharField(max_length=32, verbose_name='工单标题')),
                ('tstart_time', models.DateTimeField(auto_now_add=True, verbose_name='工单创建时间')),
                ('tfinish_time', models.DateTimeField(null=True, verbose_name='工单关闭时间')),
                ('tcontent', models.CharField(max_length=90, null=True, verbose_name='工单内容')),
                ('tis_finished', models.BooleanField(default=False, verbose_name='是否完成')),
                ('tcreater', models.CharField(max_length=64, null=True, verbose_name='创建人')),
                ('ttimeused', models.FloatField(default=0, verbose_name='耗时')),
                ('tproject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.Projects', verbose_name='项目名称')),
            ],
            options={
                'verbose_name': '工单',
                'verbose_name_plural': '工单',
            },
        ),
    ]
