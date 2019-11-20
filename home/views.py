from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Member
from .forms import MemberForm, RegisterForm
# Create your views here.
def index(request):
    return render(request, 'pet/index.html')

#1119
import hashlib

def hash_code(s, salt='ivan'): #密碼加密
    h = hashlib.sha256()
    s = s + salt
    h.update(s.encode())
    return h.hexdigest()

def login(request):
    if request.session.get('is_login',None): #檢查session確定是否登入，不允許重複登入
    #若已登入則導向主頁
        return redirect('/')
    if request.method == 'POST':    #接收POST訊息，若無則讓返回空表單
        login_form = MemberForm(request.POST)   #導入表單模型
        if login_form.is_valid(): #驗證表單
            username = login_form.cleaned_data['username']  #從表單的cleaned_data中獲得具體值
            password = login_form.cleaned_data['password'] 
            try:
                user = Member.objects.get(name=username)
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
    login_form = MemberForm(request.POST) #返回空表單
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
            if password != checkpassword: #若兩次密碼不同
                message = "兩次輸入的密碼不同!"
                return render(request, 'registration/register.html', locals())
            else:
                same_name_user = Member.objects.filter(name=username) #比對資料庫是否有相同用戶名
                if same_name_user:
                    message = "該用戶名稱已存在!"
                    return render(request, 'registration/register.html', locals())
                same_email_user = Member.objects.filter(email=email)  #比對資料庫是否有相同信箱
                if same_email_user:
                    message = "信箱已被使用!"
                    return render(request, 'registration/register.html', locals())
                #若上面條件皆通過，則創建新的用戶
                new_user = Member()
                new_user.name = username
                new_user.password = hash_code(password)
                new_user.email = email
                new_user.address = address
                new_user.sex = sex
                new_user.save()
                #自動跳轉到登入頁面
                return render(request, "registration/login.html")
    register_form = RegisterForm(request.POST)
    return render(request, 'registration/register.html', locals())