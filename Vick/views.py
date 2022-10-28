from django.shortcuts import render,HttpResponse
from django.urls import resolve
from Vick.models import Calors
import random
# Create your views here.
def home(request):
    varu ={
        'variable':f"{random.randint(1, 100)}"
    }
    return render(request, 'cool.html')

def blogs(request):
    akul = {
        "data": Calors.objects.all()
    }
    return render(request, 'blogs.html', akul)

def Blogposts(request, slug=None):
    objs = None
    if slug is not None:
        objs = Calors.objects.get(slug=slug)
    context = {
        'kola':objs
    }
    return render(request, 'lord.html', context)


