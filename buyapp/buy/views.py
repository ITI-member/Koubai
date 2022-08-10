from django.shortcuts import render,redirect
from .forms import DeptCreateForm
from .models import DeptMaster

def index(request):
    return render(request,'buy/index.html')

def dept(request):
    return render(request,'buy/dept.html')

def deptadd(request):
    form = DeptCreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('buy:index')

    context= {
        'form':form
    }
    return render(request,'buy/dept_form.html',context)