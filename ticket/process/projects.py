from django.shortcuts import render, redirect, HttpResponse
from ..models import Projects


def create_projects(request):
    if request.method == "GET":
        return render(request, 'create_projects.html')
    elif request.method == "POST":
        # 避免重复添加项目信息
        if Projects.objects.filter(pname=request.POST.get("pname", None)):
            return render(request, 'create_projects.html', {'msg': "已有此项目相关信息"})
        else:
            Projects.objects.create(pname=request.POST.get("pname", None),
                                    pstage=request.POST.get("pstage", None),
                                    pcity=request.POST.get("pstage", None),
                                    poperator=request.POST.get("poperator", None),
                                    pdeveloper=request.POST.get("pdeveloper", None),
                                    psales=request.POST.get("psales", None),
                                    pmanager=request.POST.get("pmanager", None),
                                    pbusiness=request.POST.get("pbusiness", None),
                                    pagent=request.POST.get("pagent", None),
                                    pimplementer=request.POST.get("pimplementer", None),
                                    pstatus=request.POST.get("pstatus", None),
                                    pprogress=request.POST.get("pprogress", None),
                                    pstart_time=request.POST.get("pstart_time", None),
                                    ponline_time=request.POST.get("ponline_time", None),
                                    pacceptance_time=request.POST.get("pacceptance_time", None),
                                    plicense_time=request.POST.get("plicense_time", None),
                                    plicexpire_time=request.POST.get("plicexpire_time", None),
                                    pexpire_time=request.POST.get("pexpire_time", None),
                                    psup_type=request.POST.get("psup_type", None))
            return redirect('create_projects')


def projects(request):
    if request.method == "GET":
        return render(request, 'projects.html', {'projects': Projects.objects.all()})
    elif request.method == "POST":
        print(request.POST)
        Projects.objects.filter(pid=request.POST.get("pid", None)) \
            .update(pstage=request.POST.get("pstage", None),
                    pcity=request.POST.get("pstage", None),
                    poperator=request.POST.get("poperator", None),
                    pdeveloper=request.POST.get("pdeveloper", None),
                    psales=request.POST.get("psales", None),
                    pmanager=request.POST.get("pmanager", None),
                    pbusiness=request.POST.get("pbusiness", None),
                    pagent=request.POST.get("pagent", None),
                    pimplementer=request.POST.get("pimplementer", None),
                    pstatus=request.POST.get("pstatus", None),
                    pprogress=request.POST.get("pprogress", None),
                    pstart_time=request.POST.get("pstart_time", None),
                    ponline_time=request.POST.get("ponline_time", None),
                    pacceptance_time=request.POST.get("pacceptance_time", None),
                    plicense_time=request.POST.get("plicense_time", None),
                    plicexpire_time=request.POST.get("plicexpire_time", None),
                    pexpire_time=request.POST.get("pexpire_time", None),
                    psup_type=request.POST.get("psup_type", None))
        return redirect('projects')
