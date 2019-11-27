from django import forms
from .models import Pet
from django.utils.translation import gettext_lazy as _ 

class UploadForm(forms.ModelForm):
    photo = forms.ImageField(label='上傳寵物照')
    class Meta:
        # 我要使用哪一個 Model
        model = Pet
        # 使用 Model 的哪些欄位
        fields = '__all__'
        # 新增 labels 對應
        labels = {
            'animal_type':_('種類'),
            'chip_num':_('晶片號碼'),
            'sex':_('性別'),
            'age':_('年紀'),
            # 'size':_('體型'),
            # 'color':_('毛色'),
            'location':_('來源地'),
            # 'neuter':_('有無結紮'),
            'health':_('健康狀態'),
            'note':_('備註'),
        }

# class RegisterForm(forms.Form):
#     gender = (
#         ('male','男'),
#         ('female','女'),
#     )
#     username = forms.CharField(label="用戶名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(label="密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     checkpassword = forms.CharField(label="確認密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     address = forms.CharField(label="地址", max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(label = "信箱", max_length=256, widget=forms.EmailInput(attrs={'class':'form-control'}))
#     sex = forms.ChoiceField(label = "性別",choices=gender)
