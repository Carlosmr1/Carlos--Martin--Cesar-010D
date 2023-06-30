from django.shortcuts import render, redirect

from .cart import Carrito
from .models import Tablegames, Videogames, User
from django.utils import timezone
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.




def post_list(request):
    posts = Tablegames.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'web/post_list.html', {'posts':posts})

def index(request):
    return render(request,'web/index.html',{})

def juegos(request):
    productos = Videogames.objects.all()
    posts = Videogames.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'web/juegos.html',{'posts':posts, "productos":productos})


def tableGames(request):
    productos = Tablegames.objects.all()
    posts = Tablegames.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'web/tableGame.html',{"posts":posts, "productos":productos})

def agregar_producto(request, producto_nombre):
    carrito = Carrito(request)
    producto = Tablegames.objects.get(nombre = producto_nombre)
    carrito.agregar(producto)
    return redirect('../juegosMesa/')
def agregar_producto(request, producto_nombre):
    carrito = Carrito(request)
    producto = Videogames.objects.get(nombre = producto_nombre)
    carrito.agregar(producto)
    return redirect('juegos')

def eliminar_producto(request, producto_nombre):
    carrito = Carrito(request)
    producto = Tablegames.objects.get(nombre = producto_nombre)
    carrito.eliminar(producto)
    return redirect('../juegosMesa/')
def eliminar_producto(request, producto_nombre):
    carrito = Carrito(request)
    producto = Videogames.objects.get(nombre = producto_nombre)
    carrito.eliminar(producto)
    return redirect('../juegos/')

def restar_producto(request, producto_nombre):
    carrito = Carrito(request)
    producto = Tablegames.objects.get(nombre = producto_nombre)
    carrito.restar(producto)
    return redirect('../juegosMesa/')
def restar_producto(request, producto_nombre):
    carrito = Carrito(request)
    producto = Videogames.objects.get(nombre = producto_nombre)
    carrito.restar(producto)
    return redirect('../juegos/')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('../')

def cuenta(request):
    return render(request,'registro/cuenta.html',{})

# def newCuenta(request):
#     return render(request, 'web/newUser.html',{})

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
    posts = Videogames.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'web/carrito.html',{'posts': posts })