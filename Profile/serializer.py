from rest_framework import routers, serializers, viewsets

#---------------- AGREGANDO MODELOS ---------------------
from Profile.models import Profile2
from Profile.models import Ocupacion2
from Profile.models import Genero2
from Profile.models import Estado2
from Profile.models import EstadoCivil2
from Profile.models import Ciudad2

class Example2Serializers(serializers.ModelSerializer):
    class Meta: 
        model = Profile2
        fields = ('__all__')


class Example2SerializersOcupacion(serializers.ModelSerializer):
    class Meta: 
        model = Ocupacion2
        fields = ('__all__')

class Example2SerializersGenero(serializers.ModelSerializer):
    class Meta: 
        model = Genero2
        fields = ('__all__')
class Example2SerializersCiudad(serializers.ModelSerializer):
    class Meta: 
        model = Ciudad2
        fields = ('__all__')

class Example2SerializersEstado(serializers.ModelSerializer):
    class Meta: 
        model = Estado2
        fields = ('__all__')

class Example2SerializersEstadoCivil(serializers.ModelSerializer):
    class Meta: 
        model = EstadoCivil2
        fields = ('__all__')

