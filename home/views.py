from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadForm
from .models import Pet
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'pet/index.html')

def uploadAnimal(request):
    if request.session.get('is_login', None): 
        if request.method == 'POST':
            upload_form = UploadForm(request.POST or None, request.FILES)
            if upload_form.is_valid():
                chip_num = upload_form.cleaned_data['chip_num'] 
                # animal_type = upload_form.cleaned_data['animal_type']
                # breed = upload_form.cleaned_data['breed']
                # age = upload_form.cleaned_data['age']
                # sex = upload_form.cleaned_data['sex']
                # location = upload_form.cleaned_data['sex']
                # health = upload_form.cleaned_data['health']
                # note = upload_form.cleaned_data['note']
                # photo = upload_form.cleaned_data['photo']
                
                same_chip_num = Pet.objects.filter(chip_num=chip_num) 
                if chip_num == same_chip_num:
                    message = "晶片號碼重複"
                    return render(request, 'pet/uploadAnimal.html', locals())
                else:
                    image_file = request.FILES['photo']
                    Pet = upload_form.save(commit=False)
                    Pet.photo = image_file
                    # Pets.pet_publisher = request.session.user_name
                    # Pets.pet_owner = request.session.user_name
                    Pet.save()
                    messages.success(request, '上傳成功')
                    upload_form = UploadForm() # 清空 form
                    # return redirect('/')
                    return redirect('home:animal_id', animal_id=Pet.id)
                # upload_form.save()
                # return redirect('/')
        upload_form = UploadForm()
        return render(request, 'pet/uploadAnimal.html', locals())
        # return redirect('/')
        # return HttpResponse("<p>資料新增成功！</p>")
    else:
        # return render(request, 'registration/login.html')
        return redirect('/account/login') 

def detailAnimal(request, id): #顯示寵物細節,已領養 或 登入者就是寵物擁有者時,沒有領養按鈕
    pet = get_object_or_404(Pet, id=id)
    return render(request, 'pet/detailAnimal.html', locals())
