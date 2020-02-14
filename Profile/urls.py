from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets

from Profile import views

urlpatterns = [
 
    re_path(r'Profile/$', views.Example2Profile.as_view()),
    re_path(r'EstadoCivil/$',views.Example2EstadoCivil.as_view()),
    re_path(r'Ciudad/$',views.Example2Ciudad.as_view()),
    re_path(r'Estado/$',views.ExampleEstado.as_view()),
    re_path(r'Genero/$',views.Example2Genero.as_view()),
    re_path(r'Ocupacion/$',views.Example2Ocupacion.as_view()),
]