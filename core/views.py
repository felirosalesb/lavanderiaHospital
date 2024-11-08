from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django import forms
from .models import ropaLavanderiaHospital, ropaLavanderiaExterna 


# Formulario de inicio de sesión
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

def login_view(request):
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Cambia esto a la URL deseada
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos.')

    return render(request, "core/login.html", {'form': form})

def home(request):
    return render(request, "core/home.html")

def ingresoRopa(request):
     # Obtiene los datos de los modelos
    ropa_hospital = ropaLavanderiaHospital.objects.first()  # Ajusta según tus necesidades
    ropa_externa = ropaLavanderiaExterna.objects.first()    # Ajusta según tus necesidades

    context = {
        'ropa_hospital': ropa_hospital,
        'ropa_externa': ropa_externa,
    }
    
    return render(request, "core/gestionRopa.html", context)

def reporte(request):
    return render(request, "core/reporte.html")

def perfil(request):
    return render(request, "core/perfil.html")


def actualizar_hospital(request):
    if request.method == 'POST':
        ropa_hospital = ropaLavanderiaHospital.objects.first()  # O usa el id si tienes varios
        ropa_hospital.suciio = request.POST.get('ropaSuciaHospital')
        ropa_hospital.limpio = request.POST.get('ropaLimpiaHospital')
        ropa_hospital.save()  # Esto actualizará los datos y recalculará cantidad
        return redirect('ingresoRopa')  # Redirige a la vista deseada

def actualizar_externa(request):
    if request.method == 'POST':
        ropa_externa = ropaLavanderiaExterna.objects.first()  # O usa el id si tienes varios
        ropa_externa.suciio = request.POST.get('ropaSuciaExterna')
        ropa_externa.limpio = request.POST.get('ropaLimpiaExterna')
        ropa_externa.save()  # Esto actualizará los datos y recalculará cantidad
        return redirect('ingresoRopa')  # Redirige a la vista deseada



    def get(self, request):
        ropa_hospital = Ropa.objects.get(tipo='hospital')  # Asegúrate de que el tipo esté definido en tu modelo
        ropa_externa = Ropa.objects.get(tipo='externa')
        
        data = {
            'hospital': {
                'limpio': ropa_hospital.limpio,
                'suciio': ropa_hospital.suciio,
                'cantidad': ropa_hospital.cantidad,
            },
            'externa': {
                'limpio': ropa_externa.limpio,
                'suciio': ropa_externa.suciio,
                'cantidad': ropa_externa.cantidad,
            }
        }
        return Response(data)