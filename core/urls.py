from django.urls import path
from .views import login_view, home, ingresoRopa, reporte, perfil

urlpatterns = [
    path("login/", login_view, name="login"),  # Cambié la ruta a 'login/'
    path("home/", home, name="home"),
    path("ingresoRopa/", ingresoRopa, name="ingresoRopa"),  # Añadí '/' al final
    path("reporte/", reporte, name="reporte"),  # Añadí '/' al final
    path("perfil/", perfil, name="perfil"),  # Añadí '/' al final
]
