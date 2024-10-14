from django.urls import path
from .views import *

urlpatterns = [
    path("", login, name="login"),
    path("home/", home, name="home"),
    path("ingresoRopa", ingresoRopa, name="ingresoRopa"),
    path("reporte", reporte, name="reporte"),
    path("perfil", perfil, name="perfil"),

]