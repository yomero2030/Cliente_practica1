from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets
from Login.views import CustonAuthToken

from Login.views import ExampleList2

urlpatterns = [
    re_path(r'Login/$', CustonAuthToken.as_view()),
    #Hola soy roberto


    re_path(r'example_lista2/$', ExampleList2.as_view()),
]