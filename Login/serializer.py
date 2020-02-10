from rest_framework import routers, serializers, viewsets

#---------------- AGREGANDO MODELOS ---------------------
from Login.models import Example2

class Example2Serializers(serializers.ModelSerializer):
    class Meta: 
        model = Example2
        fields = ('_all_')