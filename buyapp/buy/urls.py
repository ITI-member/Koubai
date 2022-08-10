from django.urls import path
from .import views

app_name = 'buy'

urlpatterns = [
    path('',views.index, name='index'),
    path('dept/',views.dept, name='dept'),
]
