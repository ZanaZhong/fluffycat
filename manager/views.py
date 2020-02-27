from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from account.models import Account
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
# from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from member.models import Violate


# Create your views here.
def index(request):
    # return HttpResponse("Hello, welcome to my website")
    return render(request,'manager/index.html')


def accountList(request):
    if check_Authority(request):
        try:
            AccountList = Account.objects.all()
            if Account.objects.count() == 0:
                return render(request,'manager/accountList.html', { 'message' : "尚無資料"})
            return render(request,'manager/accountList.html', {'accountList' : AccountList} )
        except:
            return render(request, 'manager/accountList.html', {'errormsg' : '沒傳到啦'})
    else:
        return render(request,'manager/error.html' )

@csrf_exempt
def suspendAccount(request):
    if request.method == 'POST':
        accountID = request.POST.getlist('id[]')
        # already = Account.objects.filter(id=accountID, suspend=True)
        # data = {
        #     'is_suspended' : " ".join(str(already.id))
        # }
        data = Account.objects.filter(id__in=accountID).update(suspend=True)

    return JsonResponse(data, safe=False)

# @csrf_protect
@csrf_exempt
def deleteAccount(request):
    if request.method == 'POST':
        # accountID = get_list_or_404(Account, id=id)
        accountID = request.POST.getlist('id[]')
        

        # accountID = request.GET.getlist('id[]', None)

        # return JsonResponse(data = account)
        data = Account.objects.filter(id__in=accountID).delete()
        # Account.objects.filter(id__in=accountID).delete()
        # data = {
        #     'is_taken': Account.objects.filter(id=accountID).exists()
        # }
        # if data['is_taken']:
        #     data['error_message'] = 'A user with this username already exists.'
        return JsonResponse(data, safe=False)
    else:
        return HttpResponse("<h1>test</h1>")

#檢舉清單
def violate_list(request):
    violate_data = Violate.objects.all()
    print(violate_data)
    if Violate.objects.count() == 0:  #沒資料
        return render(request,'manager/violate_list.html', { 'message' : "尚無資料"})
    return render(request,'manager/violate_list.html', { 'violate_data' : violate_data})


def check_Authority(request):
    try:
        User_ID = request.session['role']  #
        return True
    except:
        return False
