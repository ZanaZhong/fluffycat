from django.shortcuts import render, redirect
# 跨app import model
from account.models import Account
from home.models import Pet
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
    member = Account.objects.get(account=request.session['user_account'])
    if request.session.get('is_login', None):
        if request.method == 'POST':  
            set_pwd_form = PasswordForm(request.POST)
            if set_pwd_form.is_valid():
                enterpwd = set_pwd_form.cleaned_data['oldpassword'] 
                newpwd = set_pwd_form.cleaned_data['newpassword']
                checknewpwd = set_pwd_form.cleaned_data['checknewpassword']

                member = Account.objects.get(account=request.session['user_account'])
                old_pwd = member.password
                
                #若輸入的舊密碼不相符
                if hash_code(enterpwd) != old_pwd :
                    message = "舊密碼輸入錯誤"
                    return render(request, 'member/setpwd.html', locals())
                else :
                    if newpwd != checknewpwd: 
                        message = "兩次輸入的密碼不同!"
                        return render(request, 'member/setpwd.html', locals())
                    member.password = hash_code(newpwd)
                    member.save()
                    message = "修改成功"
                    return render(request, 'member/setpwd.html', locals())
        set_pwd_form = PasswordForm()
        # return redirect('member')
        return render(request, 'member/setpwd.html', {'member' : member, 'set_pwd_form': set_pwd_form} )
    else:
        return redirect('/account/login')

def editMember(request):
    if request.method == 'POST':
        name = request.POST['member-name']
        sex = request.POST['member-sex']
        email = request.POST['member-email']
        address = request.POST['member-address'] 

        editAccount = Account.objects.get(account=request.session['user_account'])
        editAccount.name = name
        editAccount.sex = sex
        editAccount.email = email
        editAccount.address = address
        editAccount.save()
        
        message : '編輯完成'
        return redirect('/member/center')

    else:
        try:
            member = Account.objects.get(account=request.session['user_account'])
            return render(request,'member/editMember.html', {'member' : member} )
        except:       
            return render(request, 'member/editMember.html', {'errormsg' : '沒傳到啦幹'})

# TODO LIST 送養人要存 其他自己記
def uploadAnimal(request):
    if request.session.get('is_login', None): 
        if request.method == 'POST':
            #chipNumber = request.POST['d']
            animalType = request.POST['種類']
            breed = request.POST['品種']
            age = request.POST['年齡']
            sex = request.POST['性別'] 
            location = request.POST['來源地']
            health = request.POST['健康情況']
            note = request.POST['備註']
            # state = request.POST['認養狀態']

            try:
                photo = request.FILES['圖片'] 
                print(photo)
                addPet = Pet() #需要import
                addPet.animalType = animalType   #資料庫的animal_id = 使用者輸入的animal
                addPet.breed = breed
                addPet.age = age
                addPet.sex = sex
                addPet.location = location
                addPet.health = health
                addPet.note = note
                addPet.photo = photo

                addPet.save()
                return render(request, 'deliver/uploadAnimal.html', {'message': '上傳完成'}) 
            except Exception as err:
                return render(request, 'deliver/uploadAnimal.html', {'errormsg':'請上傳圖片'})
        return render(request, 'deliver/uploadAnimal.html') 

    else:
        return redirect('/account/login') 

def detailAnimal(request, id): #顯示寵物細節,已領養 或 登入者就是寵物擁有者時,沒有領養按鈕
    pet = get_object_or_404(Pet, id=id)
    return render(request, 'deliver/detailAnimal.html', locals())