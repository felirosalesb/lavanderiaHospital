from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django import forms

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
    return render(request, "core/gestionRopa.html")

def reporte(request):
    return render(request, "core/reporte.html")

def perfil(request):
    return render(request, "core/perfil.html")
