from django.db import models
from django.contrib.auth.models import AbstractUser

# Cria um usuario abstrato(já possui campos padrão de username,password,etc), com duas categorias (comum e adm) inseridas em um campo customizado
class Usuario(AbstractUser):
    CATEGORIA = [
        ('C','Comum'),
        ('A','Administrador')
    ]
    categoria = models.CharField(max_length=1,choices=CATEGORIA,default='C')

    # Ao pesquisar um usuario, ele sera identificado pelo nome ao enves do id (na tela de admin)
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

    # Ao pesquisar um Sensor, ele sera identificado pelo nome 
    def __str__(self):
        return self.sensor

# Cria um modelo para ambiente
class Ambiente(models.Model):
    sig = models.IntegerField()
    descricao = models.CharField(max_length=50)
    ni = models.CharField(max_length=50)
    responsavel = models.CharField(max_length=50)

    # Ao pesquisar o ambiente ele será identificado pelo ni(numero de identificação)
    def __str__(self):
        return self.ni

# Cria um modelo para historico
class Historico(models.Model):
    valor = models.FloatField()
    timestamp = models.DateTimeField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
