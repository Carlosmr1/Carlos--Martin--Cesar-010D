from django.shortcuts import render
from .models import Tablegames, Videogames
from django.utils import timezone
# Create your views here.
def post_list(request):
    posts = Tablegames.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'web/post_list.html', {'posts':posts})

def index(request):
    return render(request,'web/index.html',{})

def juegos(request):
    return render(request, 'web/juegos.html',{})

def tableGames(request):
    return render(request,'web/tableGame.html',{})
