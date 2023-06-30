from django.shortcuts import render, redirect
from .models import Tablegames, Videogames, User
from django.utils import timezone
from .forms import UserForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages


# Create your views here.
def post_list(request):
    posts = Tablegames.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'web/post_list.html', {'posts':posts})

def index(request):
    return render(request,'web/index.html',{})

def juegos(request):
    posts = Videogames.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'web/juegos.html',{'posts':posts})


def tableGames(request):
    posts = Tablegames.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'web/tableGame.html',{"posts":posts})

def cuenta(request):
    return render(request,'registro/cuenta.html',{})



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


    
        