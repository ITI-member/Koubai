from multiprocessing import context
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
'''/トップページ'''
def index(request):
    context = {
        'name': 'sacota',
    }
    return render(request,'myapp/index.html',context)
'''/about アバウトページ'''
def about(request):
    return render(request,'myapp/about.html')

'''/info インフォページ'''
def info(request):
    return render(request,'myapp/info.html')