from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Curso, Interesse, Perfil

admin.site.register(Curso)
admin.site.register(Interesse)
admin.site.register(Perfil)