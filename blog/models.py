from tkinter import CASCADE
from django.db import models

# Create your models here.

from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Interesse(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    
    def __str__(self):
        return self.titulo

class Perfil(models.Model):
    nome = models.CharField(max_length=100)
    biografia = models.TextField()
    imagem = models.ImageField(upload_to='perfil/', null=True, blank=True)
    interesses = models.ManyToManyField(Interesse)
    cursos = models.ManyToManyField(Curso)
    
    def __str__(self):
        return self.nome