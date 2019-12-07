from django import forms
from django.utils.translation import gettext_lazy as _ 

class PasswordForm(forms.Form):
    oldpassword = forms.CharField(label="舊密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    newpassword = forms.CharField(label="新密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    checknewpassword = forms.CharField(label="確認新密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
