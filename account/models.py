from django.db import models
from django.contrib import admin
from django.urls import reverse
# Create your models here.

class Account(models.Model):
    gender = (
        ('male','男'),
        ('female','女'),
    )
    role_choice = (
        ('member', '一般會員'),
        ('admin', '管理員'),
    )
    suspend_choice = (
        (True, '停權'),
        (False, '正常'),
    )
    name = models.CharField(max_length=128)
    account = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
    sex = models.CharField(max_length=32,choices=gender,default="男")
    email = models.EmailField(unique=True)
    address = models.CharField(max_length = 150)
    role = models.CharField(max_length=32,choices=role_choice,default="一般會員")
    suspend = models.BooleanField('是否停權',choices=suspend_choice,default=False)
    ctime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " " + self.account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Account._meta.fields]
# admin.site.register(Accounts,AccountAdmin)

