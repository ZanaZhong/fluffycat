from django.db import models
from django.contrib import admin
from django.urls import reverse
# Create your models here.

class Account(models.Model):
    gender = (
        ('male','男'),
        ('female','女'),
    )
    name = models.CharField(max_length=128)
    account = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
    sex = models.CharField(max_length=32,choices=gender,default="男")
    email = models.EmailField(unique=True)
    address = models.CharField(max_length = 150)
    ctime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Account._meta.fields]
# admin.site.register(Accounts,AccountAdmin)

class Violate(models.Model):
    vlist = (
        ('圖文不符','圖文不符'),
        ('洗版','洗版'),
        ('其他','其他'),
    )
    name = models.CharField('名字', max_length=32)
    violateList = models.CharField(max_length=32,choices=vlist,default="圖文不符")

    def __str__(self):
        return self.id

@admin.register(Violate)
class ViolateAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Violate._meta.fields]
