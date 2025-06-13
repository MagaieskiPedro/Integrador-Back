from django.urls import path, include
from . import views
from .views import SensoresView,AmbientesView,HistoricosView
from rest_framework import routers

# Instancia router para receber rotas geradas pelo ModelViewSet(Gera CRUD completo com uma unica classe)
router = routers.DefaultRouter()

# Registra rotas/urls geradas pelo ModelViewSet na instancia de router
router.register(r"sensores",SensoresView, basename="Sensor")
router.register(r"ambientes", AmbientesView , basename="Ambiente")
router.register(r"historicos", HistoricosView , basename="Historico")

# Inclui as urls regisradas em router, e cria urls para os endpoints das views de login e cadastro
urlpatterns = [
    path("",include(router.urls)),
    path('login/', view=views.LoginView.as_view()),
    path('cadastro/', view=views.CadastroView.as_view())
]