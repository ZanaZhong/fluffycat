from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadForm
from .models import Pet
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json, os, sys
import requests

# Create your views here.
def index(request):
    try:
        pet = Pet.objects
        return render(request,'pet/index.html', {'pet' : pet} )
    except:       
        return render(request, 'pet/index.html', {'errormsg' : '沒傳到啦幹'})

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
                #addPet.animalType = animalType   #資料庫的animal_id = 使用者輸入的animal
                addPet.breed = breed
                #addPet.age = age
                #addPet.sex = sex
                #addPet.location = location
                addPet.health = health
                addPet.note = note
                addPet.photo = photo

                addPet.save()
                return render(request, 'pet/uploadAnimal.html', {'message': '上傳完成'}) 
            except Exception as err:
                return render(request, 'pet/uploadAnimal.html', {'errormsg':'請上傳圖片'})
        return render(request, 'pet/uploadAnimal.html') 

    else:
        return redirect('/account/login') 

# # @login_required
# def uploadAnimal(request):
#     if request.session.get('is_login', None): 
#         if request.method == 'POST':
#             upload_form = UploadForm(request.POST or None, request.FILES)
#             print(upload_form.errors)
#             print(upload_form.is_valid())
#             if upload_form.is_valid():
#                 chipNum = upload_form.cleaned_data['chipNum'] 
#                 animalType = upload_form.cleaned_data['animalType']
#                 breed = upload_form.cleaned_data['breed']
#                 age = upload_form.cleaned_data['age']
#                 sex = upload_form.cleaned_data['sex']
#                 location = upload_form.cleaned_data['sex']
#                 health = upload_form.cleaned_data['health']
#                 note = upload_form.cleaned_data['note']
#                 photo = upload_form.cleaned_data['photo']
#                 # print(animal_type)
                
#                 same_chip_num = Pet.objects.filter(chip_num=chip_num) 
#                 if chip_num == same_chip_num:
#                     message = "晶片號碼重複"
#                     return render(request, 'pet/uploadAnimal.html', locals())
#                 else:
#                     image_file = request.FILES['photo']
#                     Pet = upload_form.save(commit=False)
#                     Pet.photo = image_file
#                     # Pets.pet_publisher = request.session.user_name
#                     # Pets.pet_owner = request.session.user_name
#                     Pet.save()
#                     messages.success(request, '上傳成功')
#                     upload_form = UploadForm() # 清空 form
#                     # return redirect('/')
#                     return redirect('home:animal_id', animal_id=Pet.id)
#                 # upload_form.save()
#                 # return redirect('/')
#         upload_form = UploadForm()
#         return render(request, 'pet/uploadAnimal.html', locals())
#         # return redirect('/')
#         # return HttpResponse("<p>資料新增成功！</p>")
#     else:
#         # return render(request, 'registration/login.html')
#         return redirect('/account/login') 

#顯示寵物細節
def detailAnimal(request, id): 
    pet = get_object_or_404(Pet, id=id)
    return render(request, 'pet/detailAnimal.html', locals())

