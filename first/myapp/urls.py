from django.urls import path
from .import views

app_name = 'myapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about ,name='about'),
    path('info/',views.info ,name='info'),
]

