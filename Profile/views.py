from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
# Create your views here.

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework import generics

from Profile.models import Profile2
from Profile.models import Ocupacion2
from Profile.models import Genero2
from Profile.models import Ciudad2
from Profile.models import Estado2
from Profile.models import EstadoCivil2
from Profile.serializer import Example2Serializers
from Profile.serializer import Example2SerializersOcupacion
from Profile.serializer import Example2SerializersGenero
from Profile.serializer import Example2SerializersCiudad
from Profile.serializer import Example2SerializersEstado
from Profile.serializer import Example2SerializersEstadoCivil


class Example2Ocupacion(APIView):
    def get(self, request , format = None):
        print ("metodo get filter")
        queryset = Ocupacion2.objects.filter(delete = False)
        #many true si se aplica retornos multiples objetos
        serializer = Example2SerializersOcupacion(queryset, many= True)
        return Response(serializer.data)

    def post(self,request, format = None):
        serializer = Example2SerializersOcupacion(data = request.data)
        if serializer .is_valid():
            serializer.save()
            data =  serializer.data
            return Response(data)
        return Response(serializer.errors , status = status.Http_400_BAD_REQUEST)
#class Genero 
class Example2Genero(APIView):

    def get(self, request , format = None):
        print ("metodo get filter")
        queryset = Genero2.objects.filter(delete = False)
        #many true si se aplica retornos multiples objetos
        serializer = Example2SerializersGenero(queryset, many= True)
        return Response(serializer.data)

    def post(self,request, format = None):
        serializer = Example2SerializersGenero(data = request.data)
        if serializer .is_valid():
            serializer.save()
            data =  serializer.data
            return Response(data)
        return Response(serializer.errors , status = status.Http_400_BAD_REQUEST)

class Example2Ciudad (APIView):
    def get(self, request , format = None):
        print ("metodo get filter")
        queryset = Ciudad2.objects.filter(delete = False)
        serializer = Example2SerializersCiudad(queryset, many= True)
        return Response(serializer.data)

    def post(self,request, format = None):
        serializer = Example2SerializersCiudad(data = request.data)
        if serializer .is_valid():
            serializer.save()
            data =  serializer.data
            return Response(data)
        return Response(serializer.errors , status = status.Http_400_BAD_REQUEST)

class ExampleEstado (APIView):
    def get(self, request , format = None):
        print ("metodo get filter")
        queryset = Estado2.objects.filter(delete = False)
        serializer = Example2SerializersEstado(queryset, many= True)
        return Response(serializer.data)

    def post(self,request, format = None):
        serializer = Example2SerializersEstado(data = request.data)
        if serializer .is_valid():
            serializer.save()
            data =  serializer.data
            return Response(data)
        return Response(serializer.errors , status = status.Http_400_BAD_REQUEST)

class Example2EstadoCivil(APIView):
    def get(self, request , format = None):
        print ("metodo get filter")
        queryset = EstadoCivil2.objects.filter(delete = False)
        serializer = Example2SerializersEstadoCivil(queryset, many= True)
        return Response(serializer.data)

    def post(self,request, format = None):
        serializer = Example2SerializersEstadoCivil(data = request.data)
        if serializer .is_valid():
            serializer.save()
            data =  serializer.data
            return Response(data)
        return Response(serializer.errors , status = status.Http_400_BAD_REQUEST)


#metodo de get 
class Example2Profile(APIView):
    #metodo get para solicitud
    def get(self, request, format = None):
        print ("metodo get filter")
        queryset = Profile2.objects.filter(delete = False)
        #many true si se aplica retornos multiples objetos
        serializer = Example2Serializers(queryset, many= True)
        return Response(serializer.data)

    def post(self,request, format = None):
        serializer = Example2Serializers(data = request.data)
        if serializer .is_valid():
            serializer.save()
            data =  serializer.data
            return Response(data)
        return Response(serializer.errors , status = status.Http_400_BAD_REQUEST)




        