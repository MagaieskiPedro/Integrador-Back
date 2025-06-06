from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action 
from django.utils import timezone

from .serializers import SensoresSerializer,AmbientesSerializer,HistoricoSerializer,LoginSerializer,CadastroSerializer
from .models import Sensor,Ambiente,Historico,Usuario
from .permissions import isAdmin,isComum,isAuthenticated
from .renderers import ExcelSensorDataRenderer

# Create your views here.
# SENSOR
class SensoresView(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensoresSerializer
    permission_classes = [isAdmin]

    @action(detail=False, methods=["get"],renderer_classes=[ExcelSensorDataRenderer])
    def download(self, request):
        queryset = self.get_queryset()
        serializer = SensoresSerializer(queryset, many=True)
        now = timezone.now()        
        file_name = f"sensor_data_archive_{now:%Y-%m-%d_%H-%M-%S}.{request.accepted_renderer.format}"

        return Response(serializer.data, headers={"Content-Disposition": f'attachment; filename="{file_name}"'})
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