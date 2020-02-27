from django.db import models
from account.models import Account
from django.contrib import admin
from home.models import Pet

# Create your models here.
class AdoptList(models.Model):
    status = (
        (0, '待批准'),
        (1, '通過'),
        (2, '拒絕'),
    )
    adoptPerson = models.ForeignKey(Account, on_delete=models.CASCADE)
    adoptPet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    status = models.IntegerField('審核狀態', choices=status, default=0)

@admin.register(AdoptList)
class AdoptListAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AdoptList._meta.fields]

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