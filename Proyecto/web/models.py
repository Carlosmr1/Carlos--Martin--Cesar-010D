from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Videogames(models.Model):
    marca = models.ForeignKey(Marca,on_delete=models.PROTECT)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos', null=True)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre
    
class Tablegames(models.Model):
    marca = models.ForeignKey(Marca,on_delete=models.PROTECT)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos', null=True)
    published_date = models.DateTimeField(
            blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre