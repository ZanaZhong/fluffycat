from django.shortcuts import render, redirect
from .models import Account
from .forms import AccountForm, RegisterForm, PasswordForm
from django.contrib.auth.decorators import login_required
# Create your views here.

#1123
import hashlib

def hash_code(s, salt='ivan'): #密碼加密
    h = hashlib.sha256()
    s = s + salt
    h.update(s.encode())
    return h.hexdigest()

def login(request):
    #檢查session確定是否登入，不允許重複登入
    if request.session.get('is_login', None): 
        # nothing happened @@ <- set_expiry
        request.session.set_expiry(0)
        #若已登入則導向主頁
        return redirect('/')
        
    if request.method == 'POST':    #接收POST訊息，若無則讓返回空表單
        login_form = AccountForm(request.POST)   #導入表單模型
        if login_form.is_valid(): #驗證表單
            useraccount = login_form.cleaned_data['useraccount']  #從表單的cleaned_data中獲得具體值
            password = login_form.cleaned_data['password'] 
            try:
                user = Account.objects.get(account=useraccount)
                if user.password == hash_code(password) and user.suspend == False: #密文處理
                    #使用session寫入登入者資料
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_account'] = user.account
                    request.session['user_name'] = user.name
                    message = "登入成功"
                    if user.role == "admin":
                        request.session['role'] = "admin"
                        return redirect('manager:index')
                    return redirect('/')
                else:
                    message = "密碼不正確"
            except:
                message = "該帳號不存在"
    login_form = AccountForm() #返回空表單
    # 為了彈入視窗改
    # return render(request,"pet/index.html",locals())
    return render(request,"registration/login.html", locals())

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
                    message = hash_code(enterpwd)
                    return render(request, 'registration/setpwd.html', locals())
                else :
                    if newpwd != checknewpwd: 
                        message = "兩次輸入的密碼不同!"
                        return render(request, 'registration/setpwd.html', locals())
                    user.password = hash_code(newpwd)
                    user.save()
                    message = "修改成功"
                    return redirect('/')
        set_pwd_form = PasswordForm()
        return render(request, 'registration/setpwd.html', locals())
    else:
        return redirect('/account/login')
def logout(request):
    if not request.session.get('is_login', None): #如果原本未登入，就不需要登出
        return redirect('/')
    request.session.flush() #一次性將session內容全部清除
    return redirect('/')

def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        message = '請檢察填寫的內容!'
        if register_form.is_valid(): #驗證數據，提取表單內容
            username = register_form.cleaned_data['username']
            useraccount = register_form.cleaned_data['useraccount'] 
            password = register_form.cleaned_data['password']
            checkpassword = register_form.cleaned_data['checkpassword']
            email = register_form.cleaned_data['email']
            address = register_form.cleaned_data['address']
            sex = register_form.cleaned_data['sex']
            #若兩次密碼不同
            if password != checkpassword: 
                message = "兩次輸入的密碼不同!"
                return render(request, 'registration/register.html', locals())
            else:
                #比對資料庫是否有相同用戶名
                same_account_user = Account.objects.filter(name=useraccount) 
                if same_account_user:
                    message = "該帳號已存在!"
                    return render(request, 'registration/register.html', locals()) 
                #比對資料庫是否有相同信箱
                same_email_user = Account.objects.filter(email=email) 
                if same_email_user:
                    message = "信箱已被使用!"
                    return render(request, 'registration/register.html', locals())
                #若上面條件皆通過，則創建新的用戶
                new_user = Account()
                new_user.name = username
                new_user.account = useraccount
                new_user.password = hash_code(password)
                new_user.email = email
                new_user.address = address
                new_user.sex = sex
                new_user.save()
                return redirect('/account/login')
    register_form = RegisterForm(request.POST)
    return render(request, 'registration/register.html', locals())