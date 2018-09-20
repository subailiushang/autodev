from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import MyUser


def userlogin(request):
    """
    处理用户登陆请求
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get("username", None)
        pwd = request.POST.get("password", None)
        user = authenticate(username=username, password=pwd)
        if user is not None:
            request.session['username'] = username
            login(request, user)
            return redirect('index')


def userlogout(request):
    logout(request)
    return render(request, 'login.html')


def userregister(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('username', None)
        job_title = request.POST.get('job_title', None)
        department = request.POST.get('department', None)
        phone = request.POST.get('phone', None)
        MyUser.objects.create_user(username=username, password=password, email=email, job_title=job_title,
                                   department=department, phone=phone)
        return redirect('login')

