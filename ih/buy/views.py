from multiprocessing import context
from django.shortcuts import render,redirect,get_object_or_404
from .forms import AddListForm, DeptCreateForm, PlaceCreateForm,DeptEditForm,PlaceEditForm
from .models import DeptMaster, PurchaserMaster,ListOfPurchases

def index(request):
    return render(request,'buy/index.html')

def dept(request):
    context ={
        'dept_list':DeptMaster.objects.all(),
    }
    return render(request,'buy/dept.html',context)

def add(request):
    form = AddListForm(request.POST or None)

    if request.method == 'POST':
        form.save()
        return redirect('buy:dept')
    context= {
        'form':form,
    }
    return render(request,'buy/add.html',context)

def deptup(request, pk):
    #urlのpkを基にdeptを取得
    dept = get_object_or_404(DeptMaster,pk=pk)
    #フォームに取得したdeptを紐づけ
    form = DeptEditForm(request.POST or None, instance=dept)
    #methot=POST、つまり送信ボタン押下時、入力内容が問題なければ
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('buy:dept')

    context = {
        'form':form,
    }
    return render(request,'buy/dept_form.html',context)


def deptadd(request):
    form = DeptCreateForm(request.POST or None)
    func = 'deptadd'
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('buy:dept')
    
    context= {
        'form':form,
        'func':func,
    }
    return render(request,'buy/dept_form.html',context)

def deptdelete(request, pk):
    #urlのpkを基にdeptを取得
    dept = get_object_or_404(DeptMaster,pk=pk)

    #methot=POST、つまり送信ボタン押下時、入力内容が問題なければ
    if request.method == 'POST':
        dept.delete()
        return redirect('buy:dept')

    context = {
        'dept':dept,
    }
    return render(request,'buy/dept_confirm_delete.html',context)

def place(request):
    context ={
        'place_list':PurchaserMaster.objects.all(),
    }
    return render(request,'buy/place.html',context)

def placeadd(request):
    form = PlaceCreateForm(request.POST or None)
    func = 'placeadd'
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('buy:place')

    context= {
        'form':form,
        'func':func
    }
    return render(request,'buy/place_form.html',context)

def placeup(request, pk):
    #urlのpkを基にdeptを取得
    place = get_object_or_404(PurchaserMaster,pk=pk)
    #フォームに取得したdeptを紐づけ
    form = PlaceEditForm(request.POST or None, instance=place)

    #methot=POST、つまり送信ボタン押下時、入力内容が問題なければ
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('buy:place')

    context = {
        'form':form,
    }
    return render(request,'buy/place_form.html',context)

def placedelete(request, pk):
    #urlのpkを基にdeptを取得
    place = get_object_or_404(PurchaserMaster,pk=pk)

    if request.method == 'POST':
        place.delete()
        return redirect('buy:place')

    context = {
        'place':place,
    }
    return render(request,'buy/place_confirm_delete.html',context)

