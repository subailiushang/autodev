from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
from ..models import Tickets, Projects


def inex(request):
    return render(request, 'base.html')


def create_ticket(request):
    user = request.session.get("username", None)
    if request.method == "GET":
        # 查询当前登录用户的数据信息
        tickets = Tickets.objects.filter(tcreater=user).values('tid', 'tproject__pname', 'tstart_time', 'tfinish_time',
                                                               'ttimeused', 'tsup_type', 'tcontent', 'tis_finished')
        return render(request, 'create_tickets.html',
                      context={"projects": Projects.objects.values('pid', 'pname'), "tickets": tickets})
    elif request.method == "POST":
        project_name = Projects.objects.get(pid=request.POST.get("tproject", None)).pname
        # send_mail("创建", '测试邮件', settings.EMAIL_FROM, ['1035127848@qq.com'], fail_silently=False)
        start_time = request.POST.get("tstart_time", None)
        support_type = request.POST.get("tsup_type", None)
        content = request.POST.get("tcontent", None)
        details = "项目名称：" + project_name + "\n创建人：" + user + "\n创建时间：" + start_time + "\n支持方式：" + support_type + "\n内容：" + content
        send_mail("创建:" + project_name + "工单", details, settings.EMAIL_FROM, ['1035127848@qq.com'], fail_silently=True)
        Tickets.objects.create(tname=request.POST.get("tname", None),
                               tproject_id=request.POST.get("tproject", None),
                               tstart_time=request.POST.get("tstart_time", None),
                               tcontent=request.POST.get("tcontent", None),
                               tsup_type=request.POST.get("tsup_type", None),
                               tcreater=user)

        # 发送邮件给此项目的项目经理
        return redirect('create_tickets')


def ticket_modal(request):
    if request.method == "POST":
        start_time = Tickets.objects.get(tid=request.POST.get("tid", None)).tstart_time
        current_time = timezone.now()
        timeused = round(((current_time - start_time).total_seconds()) / 3600, 2)
        # 0代表该工单未完成，1代表工单已经完成
        if request.POST.get("tis_finished", None) == '1':
            Tickets.objects.filter(tid=request.POST.get("tid", None)).update(
                tsup_type=request.POST.get("tsup_type", None),
                tcontent=request.POST.get("tcontent", None),
                tis_finished=request.POST.get("tis_finished", None),
                tfinish_time=current_time, ttimeused=timeused)
        else:
            Tickets.objects.filter(tid=request.POST.get("tid", None)).update(
                tsup_type=request.POST.get("tsup_type", None),
                tcontent=request.POST.get("tcontent", None),
                tis_finished=request.POST.get("tis_finished", None),
                ttimeused=timeused)
        return redirect('create_tickets')
