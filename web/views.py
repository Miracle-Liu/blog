from django.shortcuts import render,HttpResponse

# Create your views here.

from repository import models
import json
from django.core import serializers

def index(request):
    return render(request,'web/index.html')

def classify(request):
    res = models.Classify.objects.all().values()
    data = json.dumps(list(res))
    return HttpResponse(data)

def articles(request):
    res = models.Article.objects.all().values()
    for(item in res):
        item.create_time =
    data = json.dumps(list(res))
    return HttpResponse(data)





