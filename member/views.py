from django.shortcuts import render, redirect
# 跨app import model
from account.models import Account
from .forms import PasswordForm
from account.views import hash_code

def index(request):
    try:
        member = Account.objects.get(account=request.session['user_account'])
        return render(request,'member/memberCenter.html', {'member' : member} )
    except:       
        return render(request, 'member/memberCenter.html', {'errormsg' : '沒傳到啦幹'})

def setpassword(request):
    #檢查session確定是否登入，不允許重複登入
    if request.session.get('is_login', None):
        if request.method == 'POST':  
            set_pwd_form = PasswordForm(request.POST)
            if set_pwd_form.is_valid():
                enterpwd = set_pwd_form.cleaned_data['oldpassword'] 
                newpwd = set_pwd_form.cleaned_data['newpassword']
                checknewpwd = set_pwd_form.cleaned_data['checknewpassword']

                user = Account.objects.get(account=request.session['user_account'])
                old_pwd = user.password
                
                #若輸入的舊密碼不相符
                if hash_code(enterpwd) != old_pwd :
                    message = "舊密碼輸入錯誤"
                    return render(request, 'member/setpwd.html', locals())
                else :
                    if newpwd != checknewpwd: 
                        message = "兩次輸入的密碼不同!"
                        return render(request, 'member/setpwd.html', locals())
                    user.password = hash_code(newpwd)
                    user.save()
                    message = "修改成功"
                    return render(request, 'member/setpwd.html', locals())
        set_pwd_form = PasswordForm()
        # return redirect('member')
        return render(request, 'member/setpwd.html', locals())
    else:
        return redirect('/account/login')