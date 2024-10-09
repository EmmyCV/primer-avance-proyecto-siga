from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Persona)
admin.site.register(Facultad)
admin.site.register(ProgramaAcademico)
admin.site.register(Docente)
admin.site.register(Estudiante)
admin.site.register(Materia)
admin.site.register(Pensum)
admin.site.register(Grupo)
admin.site.register(AsignacionDocente)
admin.site.register(Matricula)
admin.site.register(NotaMateria)
admin.site.register(CalculadoraNotas)
admin.site.register(Notificacion)