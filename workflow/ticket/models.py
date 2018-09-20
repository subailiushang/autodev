from django.db import models
from django.contrib.auth.models import AbstractUser


# 扩展系统django的user用户表
class MyUser(AbstractUser):
    job_title = models.CharField(max_length=32, verbose_name="职位")
    department = models.CharField(max_length=32, verbose_name="部门")
    phone = models.CharField(verbose_name="手机号码", null=True, max_length=20)


# 项目表
class Projects(models.Model):
    pid = models.AutoField(primary_key=True, verbose_name="项目编号")
    pname = models.CharField(max_length=200, verbose_name="项目名称")
    pstage = models.CharField(max_length=32, verbose_name="项目阶段")
    pcity = models.CharField(max_length=32, verbose_name="城市")
    poperator = models.CharField(max_length=32, verbose_name="运维")
    pdeveloper = models.CharField(max_length=32, verbose_name="开发")
    psales = models.CharField(max_length=32, verbose_name="销售")
    pmanager = models.CharField(max_length=32, verbose_name="项目经理")
    pbusiness = models.CharField(max_length=32, verbose_name="业务")
    pagent = models.CharField(max_length=64, verbose_name="代理商", null=True)
    pimplementer = models.CharField(max_length=64, verbose_name="实施方")
    pstatus = models.CharField(max_length=64, verbose_name="项目状态")
    # 项目进展为txt保存格式
    pprogress = models.TextField(verbose_name="项目进展")
    # 项目时间管理
    pstart_time = models.DateField(verbose_name="开始时间")
    ponline_time = models.DateField(verbose_name="上线时间", null=True)
    pacceptance_time = models.DateField(verbose_name="验收时间", null=True)
    plicense_time = models.CharField(max_length=32, verbose_name="授权时长")
    plicexpire_time = models.DateField(verbose_name="授权到期时间")
    pexpire_time = models.DateField(verbose_name="维保到期时间", null=True)
    psup_type = models.CharField(verbose_name="支持方式", max_length=32)

    def __str__(self):
        return self.pname

    class Meta:
        verbose_name = "项目"
        verbose_name_plural = verbose_name


class Tickets(models.Model):
    tid = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=32, verbose_name="工单标题")
    tproject = models.ForeignKey(Projects, on_delete=models.CASCADE, verbose_name="项目名称")
    tstart_time = models.DateTimeField(verbose_name="工单创建时间")
    tfinish_time = models.DateTimeField(verbose_name="工单关闭时间", null=True)
    tcontent = models.TextField(verbose_name="工单内容")
    tis_finished = models.BooleanField(verbose_name="是否完成", default=False)
    tcreater = models.CharField(verbose_name="创建人", max_length=64, null=True)
    ttimeused = models.FloatField(verbose_name="耗时", null=True)
    tsup_type = models.CharField(verbose_name="支持方式", max_length=32)

    def __str__(self):
        return self.tname

    class Meta:
        verbose_name = "工单"
        verbose_name_plural = verbose_name
