from django.shortcuts import render, redirect

from .cart import Carrito
from .models import Productos, User
from django.utils import timezone
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages

# Create your views here.





def index(request):
    return render(request,'web/index.html',{})

def tableGames(request):
    productos = Productos.objects.filter(categoria__tipo__icontains ='mesa')
    return render(request, 'web/tableGame.html',{"productos":productos})

def juegos(request):
    productos = Productos.objects.filter(categoria__tipo__icontains='VideoJuegos')
    return render(request, 'web/juegos.html',{"productos":productos})


def agregar_producto(request, producto_nombre):
    carrito = Carrito(request)
    producto = Productos.objects.get(nombre = producto_nombre)
    carrito.agregar(producto)
    return redirect('../carrito')

def eliminar_producto(request, producto_nombre):
    carrito = Carrito(request)
    producto = Productos.objects.get(nombre = producto_nombre)
    carrito.eliminar(producto)
    return redirect('../carrito')

def restar_producto(request, producto_nombre):
    carrito = Carrito(request)
    producto = Productos.objects.get(nombre = producto_nombre)
    carrito.restar(producto)
    return redirect('../carrito')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('../')

def cuenta(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            contrasena = form.cleaned_data['contrasena']
            user = authenticate(request, username=usuario, password=contrasena)
            if user is not None:
                login(request, user)
                return redirect('../')  #lo manda al inicio
            else:
                form.add_error(None, 'Credenciales inválidas')
    else:
        form = LoginForm()
    return render(request, 'registro/cuenta.html', {'form': form}) 

def newCuenta(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            correo = form.cleaned_data['correo']
            contrasena = form.cleaned_data['contrasena']
            confirmar_contrasena = form.cleaned_data['confirmar_contrasena']
            
            if contrasena == confirmar_contrasena:
                
                contrasena_segura = make_password(contrasena)
                
                
                user = User(usuario=usuario, correo=correo, contrasena=contrasena_segura)
                user.save()
                
                
                return redirect('../')
    else:
        form = UserForm()
    
    return render(request, 'registro/newUser.html', {'form': form})

def nosotros(request):
    return render(request,'web/nosotros.html',{})

class registro(View):

    def get(self, request):
        form=UserCreationForm()
        return render(request,'registro/newUser.html',{'form':form})

    def post(self, request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            Usuario=form.save()

            login(request, Usuario)

            return redirect('../')
        
        else:
            pass

def carrito(request):    
    return render(request, 'web/carrito.html',{})