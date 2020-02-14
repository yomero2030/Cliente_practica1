from django.db import models

# Create your models here.
#from django.db import models
from django.utils import timezone
# Create your models here.

class Estado2 (models.Model):
    nameEstado = models.CharField(max_length=254, null = False)
    delete = models.BooleanField(default = False)
    create = models.DateTimeField(default = timezone.now)

    def _str_(self):
        return self.nameEstado

    class Meta: 
        db_table = 'estado'


class Ocupacion2 (models.Model):
    nameOcupacion = models.CharField(max_length=254, null = False)
    delete = models.BooleanField(default = False)
    create = models.DateTimeField(default = timezone.now)

    def _str_(self):
        return self.nameOcupacion

    class Meta: 
        db_table = 'ocupacion'

class EstadoCivil2 (models.Model):
    EstadoCivil =  models.CharField(max_length=254, null = False)
    delete = models.BooleanField(default = False)
    create = models.DateTimeField(default = timezone.now)

    def _str_(self):
        return self.EstadoCivil

    class Meta: 
        db_table = 'estadoCivil'

class Genero2 (models.Model):
    TipoGenero =  models.CharField(max_length=254, null = False)
    delete = models.BooleanField(default = False)
    create = models.DateTimeField(default = timezone.now)

    def _str_(self):
        return self.TipoGenero

    class Meta: 
        db_table = 'genero'

class Ciudad2 (models.Model):
    nameCiudad = models.CharField(max_length=254, null = False)
    delete = models.BooleanField(default = False)
    create = models.DateTimeField(default = timezone.now)


    def _str_(self):
        return self.nameCiudad

    class Meta: 
        db_table = 'ciudad'

class Profile2(models.Model):
    name = models.CharField(max_length=254, null = False)
    ApPat = models.CharField(max_length=254, null = False)
    ApMat = models.CharField(max_length=254, null = False)
    Edad = models.IntegerField(null = False)

    Ciudad = models.ForeignKey(Ciudad2, on_delete=models.CASCADE)
    Genero = models.ForeignKey(Genero2, on_delete=models.CASCADE)
    Estado = models.ForeignKey(Estado2, on_delete=models.CASCADE)
    Ocupacion = models.ForeignKey(Ocupacion2, on_delete=models.CASCADE)
    EstadoCivil =  models.ForeignKey(EstadoCivil2, on_delete=models.CASCADE)

    delete = models.BooleanField(default = False)
    create = models.DateTimeField(default = timezone.now)


    def _str_(self):
        return self.name

    class Meta: 
        db_table = 'profile'