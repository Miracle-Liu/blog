from django.shortcuts import render, HttpResponse
from django.db.models import Q

# Create your views here.

from repository import models
from web import froms
import json
from django.core import serializers
# 生成图片验证码
from utils.check_code import create_validate_code
from io import BytesIO

# 处理图片转base64
import base64
# from cStringIO import StringIO

# 解决ajax post 需要在请求头中带上csrf_token，页面没有用模块tag，服务器没有在Cookies返回csrf_token，利用装饰器为需要的视图函数添加scrf_token
from django.views.decorators.csrf import ensure_csrf_cookie





def imgCode(request):
    stream = BytesIO()  # 开辟一块内存空间，不用写在外存，减少读写操作
    img, code = create_validate_code()
    img.save(stream, 'PNG')
    request.session['CheckCode'] = code
    binary_data = stream.getvalue()
    base64_data = base64.b64encode(binary_data)  #还是一个bypt ，会多b''把数据包起来
    base64_data_str = str(base64_data)
    res = 'data:image/jpg;base64,%s' %(base64_data_str[2:-1])
    data={'msg':'ok','code':0,'res':res}
    return HttpResponse(json.dumps(data))


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
""" 
登录

 """
@ensure_csrf_cookie
def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        res = models.User.objects.filter(Q(name=name) and Q(password=password))
        if res:
            data = {'msg': '登录成功', 'code': 0,'res':''}
        else:
            data = {'msg': '用户名密码不正确', 'code': 1,'res':""}
        return HttpResponse(json.dumps(data))
    else:
        return render(request, 'web/login.html')

        
        
""" 注册 """        
@ensure_csrf_cookie
def register(request):
    if request.method == 'POST':
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
            return HttpResponse(json.dumps({'msg': '注册成功', 'code': 0,'res':''}))
        else:
            return HttpResponse(json.dumps({'msg': '注册失败', 'code': 1,'res':''}))
    else:
        return render(request, 'web/register.html')