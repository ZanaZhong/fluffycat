from django import forms
from .models import Pet
from django.utils.translation import gettext_lazy as _ 

# class UploadForm(forms.ModelForm):
#     photo = forms.ImageField(label='上傳寵物照')
#     class Meta:
#         # 我要使用哪一個 Model
#         model = Pet
#         # 使用 Model 的哪些欄位
#         fields = '__all__'
#         # fields = {
#         #     'animal_type',
#         #     'chip_num',
#         #     'sex',
#         #     'age',
#         #     'breed',
#         #     'location',
#         #     'health',
#         #     'note',
#         # }

#         # 新增 labels 對應
#         labels = {
#             'animalType':_('種類'),
#             'chipNum':_('晶片號碼'),
#             'sex':_('性別'),
#             'age':_('年紀'),
#             'breed':_('品種'),
#             # 'color':_('毛色'),
#             'location':_('來源地'),
#             # 'neuter':_('有無結紮'),
#             'health':_('健康狀態'),
#             'note':_('備註'),
#         }

class UploadForm(forms.Form):
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
    animalType = forms.ChoiceField(label="種類", choices=animal_type_choice)
    chipNum = forms.CharField(label="晶片號碼", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label="性別", choices=sex_choice)
    age = forms.ChoiceField(label="年齡", choices=age_choice)
    breed = forms.CharField(label="品種", max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.ChoiceField(label="來源地", choices=area_choice)
    health = forms.CharField(label="健康狀態", max_length=256, widget=forms.TextInput(attrs={'class':'form-control'}))
    note = forms.CharField(label="備註", widget=forms.Textarea(attrs={'class': 'form-control'}))
    photo = forms.ImageField(label='上傳寵物照')

