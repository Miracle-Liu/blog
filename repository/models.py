from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    interest = models.CharField(max_length=120)


class Classify(models.Model):
    name = models.CharField(max_length=32)


class Article(models.Model):
    title = models.CharField(max_length=32)
    classify = models.ForeignKey('Classify',on_delete=models.SET_NULL,null=True)
    description = models.CharField(max_length=120)
    content = models.CharField(max_length=1200)
    create_time = models.DateField(auto_now=True)
    update_time = models.DateField(auto_now_add=True)
    author = models.ForeignKey('User',on_delete=models.SET_NULL,null=True)


