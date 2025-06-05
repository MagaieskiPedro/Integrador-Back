from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
 
from .serializers import SensoresSerializer,AmbientesSerializer,HistoricoSerializer,LoginSerializer,CadastroSerializer
from .models import Sensor,Ambiente,Historico,Usuario
from .permissions import isAdmin,isComum,isAuthenticated

# Create your views here.
# SENSOR
class SensoresView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensoresSerializer
    permission_classes = [isAdmin]
class SensorView(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensoresSerializer
    lookup_field = 'pk'
    permission_classes = [isAdmin]
# AMBIENTE
class AmbientesView(ListCreateAPIView):
    queryset = Ambiente.objects.all()
    serializer_class = AmbientesSerializer
    permission_classes = [isAdmin]
class AmbienteView(RetrieveUpdateDestroyAPIView):
    queryset = Ambiente.objects.all()
    serializer_class = AmbientesSerializer
    lookup_field = 'pk'
    permission_classes = [isAdmin]

# HISTORICO
class HistoricosView(ListCreateAPIView):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
    permission_classes = [isAdmin]
class HistoricoView(RetrieveUpdateDestroyAPIView):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
    lookup_field = 'pk'
    permission_classes = [isAdmin]

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class CadastroView(CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = CadastroSerializer