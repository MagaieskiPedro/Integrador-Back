from django.db import models
from django.contrib.auth.models import AbstractUser

# Cria um usuario abstrato(já possui campos padrão de username,password,etc), com duas categorias (comum e adm) inseridas em um campo customizado
class Usuario(AbstractUser):
    CATEGORIA = [
        ('C','Comum'),
        ('A','Administrador')
    ]
    categoria = models.CharField(max_length=1,choices=CATEGORIA,default='C')
    def __str__(self):
        return self.username

# Cria um modelo para Sensor
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

# Cria um modelo para ambiente
class Ambiente(models.Model):
    sig = models.IntegerField()
    descricao = models.CharField(max_length=50)
    ni = models.CharField(max_length=50)
    responsavel = models.CharField(max_length=50)
    def __str__(self):
        return self.ni

# Cria um modelo para historico
class Historico(models.Model):
    valor = models.FloatField()
    #  $$$$$$$$$$$$$$$$$$$$$$MUDAR FORMATO PARA BATER COM O EXCEL$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    timestamp = models.IntegerField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)

    def __str__(self):
        return self.timestamp