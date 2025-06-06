from django.urls import path, include
from . import views
from .views import SensoresView
from rest_framework import routers

router = routers.DefaultRouter()
router.register("sensores",SensoresView, basename="Sensor")

urlpatterns = [
    path("",include(router.urls)),
    path('ambientes/',view=views.AmbientesView.as_view()),
    path('historicos/',view=views.HistoricosView.as_view()),
    # path('sensores/', view=views.SensoresView.as_view()),

    path('ambiente/<int:pk>',view=views.AmbienteView.as_view()),
    path('historico/<int:pk>', view=views.HistoricoView.as_view()),
    # path('sensor/<int:pk>', view=views.SensorView.as_view()),

    path('login/', view=views.LoginView.as_view()),
    path('cadastro/', view=views.CadastroView.as_view())
]