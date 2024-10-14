from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "core/login.html")

def home(request):
    return render(request, "core/home.html")

def ingresoRopa(request):
    return render(request, "core/ingresoRopa.html")

def reporte(request):
    return render(request, "core/reporte.html")

def perfil(request):
    return render(request, "core/perfil.html")

    