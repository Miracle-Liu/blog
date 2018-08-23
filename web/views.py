from django.shortcuts import render, HttpResponse
from django.db.models import Q

# Create your views here.

from repository import models
import json
from django.core import serializers


def index(request):
    return render(request, 'web/index.html')


def classify(request):
    res = models.Classify.objects.all().values()
    data = json.dumps(list(res))
    return HttpResponse(data)


def articles(request):
    classify_id = request.GET.get('classify_id')
    print(classify_id)
    if classify_id:
        res = models.Article.objects.filter(classify_id=classify_id).values('id', 'title', 'description',
                                                'create_time', 'update_time', 'author__name', 'author_id')
    else:
        res = models.Article.objects.all().values('id', 'title', 'description',
                                                'create_time', 'update_time', 'author__name', 'author_id')
    data = json.dumps(list(res))
    return HttpResponse(data)

def login(request):
    name = request.POST.get('name')
    password =request.POST.get('password')
    res = models.User.objects.filter(Q(name) and Q(password))
    print(res)
    return HttpResponse(1111)
