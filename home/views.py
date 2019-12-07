from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadForm
from .models import Pet, Shelter
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

#顯示寵物細節
def detailAnimal(request, id): 
    pet = get_object_or_404(Pet, id=id)
    return render(request, 'pet/detailAnimal.html', locals())

def update_Json_To_DB(request):
    #以下為json塞入DB
    url = "http://163.29.157.32:8080/dataset/6a3e862a-e1cb-4e44-b989-d35609559463/resource/f4a75ba9-7721-4363-884d-c3820b0b917c/download/363b8cdd1d2742768af9e47ae54a09c2.json"
    data = requests.get(url).json()
    
    count = 0;
    for item in data:
        pet = Shelter() #需要import
        if count  ==10 :
            break
        pet.Name = item['Name']
        pet.Sex = item['Sex']
        pet.Type = item['Type']
        pet.Build = item['Build']
        pet.Age = item['Age']
        pet.Variety = item['Variety']
        pet.Reason = item['Reason']
        pet.AcceptNum = item['AcceptNum']
        pet.ChipNum = item['ChipNum']
        pet.IsSterilization = item['IsSterilization']
        pet.HairType = item['HairType']
        pet.Note = item['Note']
        pet.Resettlement = item['Resettlement']
        pet.Phone = item['Phone']
        pet.Email = item['Email']
        pet.ChildreAnlong = item['ChildreAnlong']
        pet.AnimalAnlong = item['AnimalAnlong']
        pet.Bodyweight = item['Bodyweight']
        pet.ImageName = item['ImageName']

        test = item['Resettlement']
        if check_id(pet.AcceptNum):
            pet.save()
        count+=1
    return render(request, 'pet/update.html',{'message' : "成功"} )

def check_id(input_id):
    try:
        get_id =  Shelter.objects.get(AcceptNum)
        #print(get_id,"已經有了!")
        return False #有get的到代表已經有資料了
    except:
        #print(get_id,"可以存")
        return True
