from unicodedata import name
from django.urls import path
from .import views

app_name = 'buy'

urlpatterns = [
    path('',views.index, name='index'),
    path('add/',views.add, name='add'),
    path('dept/',views.dept, name='dept'),
    path('deptup/<int:pk>/',views.deptup, name='deptup'),
    path('deptadd/',views.deptadd, name='deptadd'),
    path('deptdelete/<int:pk>/',views.deptdelete, name='deptdelete'),
    path('place/',views.place, name='place'),
    path('placeadd/',views.placeadd, name='placeadd'),
    path('placeup/<int:pk>/',views.placeup, name='placeup'),
    path('placedelete/<int:pk>/',views.placedelete, name='placedelete'),
    path('purchases/',views.purchases, name='purchases'),
    path('purchasesdelete/<int:pk>/',views.purchasesdelete,name='purchasesdelete'),
    path('purchasesup/<int:pk>/',views.purchasesup, name='purchasesup'),
    path('xlsx/',views.xlsx, name='xlsx'),
]
