from django.urls import path
from .views import login_view, home, ingresoRopa, reporte, perfil, actualizar_hospital, actualizar_externa

urlpatterns = [
    path("login/", login_view, name="login"),  # Cambié la ruta a 'login/'
    path("home/", home, name="home"),
    path("ingresoRopa/", ingresoRopa, name="ingresoRopa"),  # Añadí '/' al final
    path("reporte/", reporte, name="reporte"),  # Añadí '/' al final
    path("perfil/", perfil, name="perfil"),  # Añadí '/' al final
    path('actualizar_hospital/', actualizar_hospital, name='actualizar_hospital'),
    path('actualizar_externa/', actualizar_externa, name='actualizar_externa'),
   
]
