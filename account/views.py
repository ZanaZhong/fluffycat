from django.shortcuts import render, redirect
from .models import Account
from .forms import AccountForm, RegisterForm
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
    if request.session.get('is_login',None): 
        #若已登入則導向主頁
        return redirect('/')
        
    if request.method == 'POST':    #接收POST訊息，若無則讓返回空表單
        login_form = AccountForm(request.POST)   #導入表單模型
        if login_form.is_valid(): #驗證表單
            username = login_form.cleaned_data['username']  #從表單的cleaned_data中獲得具體值
            password = login_form.cleaned_data['password'] 
            try:
                user = Account.objects.get(name=username)
                if user.password == hash_code(password): #密文處理
                    #使用session寫入登入者資料
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    message = "登入成功"
                    return redirect('/')
                else:
                    message = "密碼不正確"
            except:
                message = "該用戶不存在"
    login_form = AccountForm(request.POST) #返回空表單
    # 為了彈入視窗改
    # return render(request,"pet/index.html",locals())
    return render(request,"registration/login.html",locals())

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
                same_name_user = Account.objects.filter(name=username) 
                if same_name_user:
                    message = "該用戶名稱已存在!"
                    return render(request, 'registration/register.html', locals()) 
                #比對資料庫是否有相同信箱
                same_email_user = Account.objects.filter(email=email) 
                if same_email_user:
                    message = "信箱已被使用!"
                    return render(request, 'registration/register.html', locals())
                #若上面條件皆通過，則創建新的用戶
                new_user = Account()
                new_user.name = username
                new_user.password = hash_code(password)
                new_user.email = email
                new_user.address = address
                new_user.sex = sex
                new_user.save()
                #自動跳轉到登入頁面 -> 會怪怪的 改跳回首頁好了
                # return render(request, "registration/login.html")
                return redirect('/')
    register_form = RegisterForm(request.POST)
    return render(request, 'registration/register.html', locals())