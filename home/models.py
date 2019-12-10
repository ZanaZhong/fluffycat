from django.db import models
from django.contrib import admin
from django.urls import reverse

# Create your models here.
class Shelter(models.Model):
    Name = models.CharField('名字', max_length=20, blank=True)
    Sex = models.CharField('性別', max_length=20, blank=True)
    Type = models.CharField('種類', max_length=20, blank=True)
    Build = models.CharField('體型', max_length=20, default='')
    Age = models.CharField('年紀', max_length=20, blank=True)
    Variety = models.CharField('品種', max_length=20, blank=True)
    Reason = models.CharField('理由', max_length=20, blank=True)
    AcceptNum = models.CharField('什麼', max_length=20, blank=True)
    ChipNum = models.CharField('晶片號碼', max_length=20, blank=True)
    IsSterilization = models.CharField('是否有結紮', max_length=20, blank=True)
    HairType = models.CharField('毛色', max_length=20, default='')
    Note = models.TextField('備註', blank=True)
    Resettlement = models.CharField('收容所編號', max_length=30, blank=True)
    Phone = models.CharField('電話', max_length=20, blank=True)
    Email = models.EmailField('信箱', blank=True)
    ChildreAnlong = models.CharField('不知道1', max_length=20, blank=True)
    AnimalAnlong = models.CharField('不知道2', max_length=20, blank=True)
    Bodyweight = models.CharField('體重', max_length=20, blank=True)
    ImageName = models.ImageField(upload_to = 'pet/')
    
    def __unicode__(self):
        return self.id
@admin.register(Shelter)
class ShelterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Shelter._meta.fields]

class Pet(models.Model):
    pet_status_choice = (
        (0, '待認養'),
        (1, '已領養'),
        
    )
    # neuter_choice = (
    #     (True, '有'),
    #     (False, '無'),
    # )
    animal_type_choice = (
        (0, '狗'),
        (1, '貓'),
        (2, '其他'),
    )
    sex_choice = (
        ('male','公'),
        ('female','母'),
    )
    area_choice = (
        (0, '台北市'),
        (1, '新北市'),
        (2, '桃園市'),
        (3, '新竹縣'),
        (4, '新竹市'),
        (5, '苗栗縣'),
        (6, '台中市'),
        (7, '彰化縣'),
        (8, '南投縣'),
        (9, '雲林縣'),
        (10, "嘉義縣"),
        (11, '嘉義市'),
        (12, '台南市'),
        (13, '高雄市'),
        (14, '屏東縣'),
        (15, '台東縣'),
        (16, '花蓮縣'),
        (17, '宜蘭縣'),
    )
    age_choice = (
        (0,'幼年'),
        (1,'成年'),
        (2,'老年'),
    )
    # pet_owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='current_owner',default='')
    # pet_publisher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='previous_owner',default='')
    # pet_name = models.CharField('寵物名', max_length=30, default='')
    
    chipNum = models.CharField('晶片號碼', max_length=20, blank=True)
    # neuter = models.BooleanField('是否有結紮', choices=neuter_choice, default=False)
    animalType = models.IntegerField('種類', choices=animal_type_choice, default=0)
    breed = models.CharField('品種', max_length=20, default='')
    age = models.IntegerField('年紀', choices=age_choice, default=0)
    sex = models.CharField('性別',max_length=32,choices=sex_choice, default="公")
    location = models.IntegerField('來源地', choices=area_choice, default=0)
    health = models.CharField('健康狀態', max_length=20, default='')
    note = models.TextField('備註', blank=True)
    photo = models.ImageField(upload_to='pet', null=True)
    state = models.IntegerField('領養狀態', choices=pet_status_choice, default=0)
    ctime = models.DateTimeField(auto_now_add=True)
    petOwner = models.CharField('送養人', max_length=20)

    # def __unicode__(self):
    #     return self.ctime
    def get_absolute_url(self):
        return reverse("home:animal_id", kwargs={"id": self.id})

# to coco 
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pet._meta.fields]