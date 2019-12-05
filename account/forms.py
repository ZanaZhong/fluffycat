from django import forms
from django.utils.translation import gettext_lazy as _ 


class AccountForm(forms.Form):
    useraccount = forms.CharField(label="帳號", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterForm(forms.Form):
    gender = (
        ('male','男'),
        ('female','女'),
    )
    username = forms.CharField(label="姓名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    useraccount = forms.CharField(label="帳號", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'oninput':'value=this.value.replace(/[^\\w_=#-]/g, "\");'}))
    password = forms.CharField(label="密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    checkpassword = forms.CharField(label="確認密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label="地址", max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label = "信箱", max_length=256, widget=forms.EmailInput(attrs={'class':'form-control'}))
    sex = forms.ChoiceField(label = "性別",choices=gender)

class PasswordForm(forms.Form):
    oldpassword = forms.CharField(label="舊密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    newpassword = forms.CharField(label="新密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    checknewpassword = forms.CharField(label="確認新密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

        