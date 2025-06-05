from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    CATEGORIA = [
        ('C','Comum'),
        ('A','Administrador')
    ]
    categoria = models.CharField(max_length=1,choices=CATEGORIA,default='C')
    def __str__(self):
        return self.username
# Create your models here.
class Sensor(models.Model):
    sensor = models.CharField(max_length=50)
    mac_address = models.CharField(max_length=50)
    unidade_med = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.BooleanField()
    class Meta:
        verbose_name_plural = 'Sensores'
    def __str__(self):
        return self.sensor

class Ambiente(models.Model):
    sig = models.IntegerField()
    descricao = models.CharField(max_length=50)
    ni = models.CharField(max_length=50)
    responsavel = models.CharField(max_length=50)
    def __str__(self):
        return self.ni

class Historico(models.Model):
    valor = models.FloatField()
    timestamp = models.IntegerField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)

    def __str__(self):
        return self.timestamp