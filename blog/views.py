from django.shortcuts import render

# Create your views here.

from .models import Curso, Interesse, Perfil

def home(request):
    cursos = Curso.objects.all()
    interesses = Interesse.objects.all()
    sobre = Perfil.objects.first()
    return render(request, 'index.html', {'cursos': cursos, 'interesses': interesses, 'sobre': sobre})

def sobre(request):
    sobre = Perfil.objects.first()
    return render(request, 'blog/sobre.html', {'sobre': sobre})