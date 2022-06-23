from django.shortcuts import render, HttpResponse, redirect
from myapp.models import UserInfo

# Create your views here.
def login(req):
    if req.method == 'GET':
        return render(req, 'login.html')
    else:
        username = req.POST.get('user')
        password = req.POST.get('password')
        if username == 'root' and password == '123':
            return redirect('https://www.baidu.com')
        else:
            return render(req, 'login.html', {'error_info': '登录失败'})

def orm(req):
    UserInfo.objects.create(name='王思程', password='111', age=18)
    UserInfo.objects.create(name='杨扬', password='111', age=17)
    UserInfo.objects.create(name='王若锦', password='111', age=3)

    return HttpResponse('数据表操作成功！')

def info_list(req):
    data_list = UserInfo.objects.all()
    return render(req, 'info_list.html', {'data_list': data_list})

def info_add(req):
    if req.method == 'GET':
        return render(req, 'info_add.html')

    username = req.POST.get('username')
    password = req.POST.get('password')
    age = req.POST.get('age')
    UserInfo.objects.create(name=username, password=password, age=age)
    return redirect('/info/list/')

def info_del(req):
    nid = req.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return redirect('/info/list/')

