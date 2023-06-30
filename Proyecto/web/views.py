from django.shortcuts import render
from .models import Tablegames, Videogames,TablegamesN
from django.utils import timezone
# Create your views here.
def post_list(request):
    posts = Tablegames.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'web/post_list.html', {'posts':posts})

def index(request):
    return render(request,'web/index.html',{})

def juegos(request):
    posts = Videogames.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'web/juegos.html',{'posts':posts})

def tableGamesN(request):
    posts = TablegamesN.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'web/tableGame.html',{"posts":posts})

def tableGames(request):
    return render(request,'web/tableGame.html',{})

def cuenta(request):
    return render(request,'web/cuenta.html',{})

def newCuenta(request):
    return render(request, 'web/newUser.html',{})

def nosotros(request):
    return render(request,'web/nosotros.html',{})