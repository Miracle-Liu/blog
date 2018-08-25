from django.shortcuts import render, HttpResponse
from django.db.models import Q

# Create your views here.

from repository import models
from web import froms
import json
from django.core import serializers
from utils.check_code import create_validate_code
from io import BytesIO

def imgCode(request):
    stream = BytesIO()  # 开辟一块内存空间，不用写在外存，减少读写操作
    img,code = create_validate_code()
    img.save(stream, 'PNG')
    request.session['CheckCode'] = code
    return HttpResponse(stream.getvalue())


def index(request):
    return render(request, 'web/index.html')


def classify(request):
    res = models.Classify.objects.all().values()
    data = json.dumps(list(res))
    return HttpResponse(data)


def articles(request):
    classify_id = request.GET.get('classify_id')
    if classify_id:
        res = models.Article.objects.filter(classify_id=classify_id).values('id', 'title', 'description',
                                                                            'create_time', 'update_time',
                                                                            'author__name', 'author_id')
    else:
        res = models.Article.objects.all().values('id', 'title', 'description',
                                                  'create_time', 'update_time', 'author__name', 'author_id')
    data = json.dumps(list(res))
    return HttpResponse(data)


def login(request):
    name = request.POST.get('name')
    password = request.POST.get('password')
    res = models.User.objects.filter(Q(name=name) and Q(password=password))
    if res:
        data = {'msg': '登录成功', 'code': 0}
    else:
        data = {'msg': '用户名密码不正确', 'code': 1}
    return HttpResponse(json.dumps(data))


def register(request):
    uf = froms.UserForm(request.POST)
    if uf.is_valid():
        dict = {}
        dict['name'] = uf.cleaned_data['name']
        dict['password'] = uf.cleaned_data['password']
        dict['email'] = uf.cleaned_data['email']
        dict['mobile_phone'] = uf.cleaned_data['mobile_phone']

        # name = uf.cleaned_data['name']
        # password = uf.cleaned_data['password']
        # email = uf.cleaned_data['email']
        # mobile_phone = uf.cleaned_data['mobile_phone']

        res = models.User.objects.get_or_create(**dict)
        print(res)
        return HttpResponse(json.dumps({'msg': '注册成功', 'code': 0}))
    else:
        return HttpResponse(json.dumps({'msg': '注册失败', 'code': 1}))
