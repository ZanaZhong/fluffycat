from django import forms
from django.utils.translation import gettext_lazy as _ 


class MemberForm(forms.Form):
    username = forms.CharField(label="用戶名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterForm(forms.Form):
    gender = (
        ('male','男'),
        ('female','女'),
    )
    username = forms.CharField(label="用戶名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    checkpassword = forms.CharField(label="確認密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label="地址", max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label = "信箱", max_length=256, widget=forms.EmailInput(attrs={'class':'form-control'}))
    sex = forms.ChoiceField(label = "性別",choices=gender)