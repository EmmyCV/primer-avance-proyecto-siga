from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    correo = models.EmailField()
    tipo_documento = models.CharField(max_length=50)
    numero_documento = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
   # Clase Facultad
class Facultad(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
   # Clase Programa academico  
class ProgramaAcademico(models.Model):
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    director = models.ForeignKey('Docente', on_delete=models.SET_NULL, null=True, related_name='programas_dirigidos')

    def __str__(self):
        return self.nombre
    
    # Clase Docente
class Docente(Persona):
    tipo_docente = models.CharField(max_length=50)
    materias_dictadas = models.ManyToManyField('Materia', through='AsignacionDocente')

    def __str__(self):
        return f"{self.nombre} - {self.tipo_docente}"
    
    # Clase Estudiante
class Estudiante(Persona):
    codigo = models.CharField(max_length=50)
    programa_academico = models.ForeignKey(ProgramaAcademico, on_delete=models.CASCADE)
    pensum = models.ForeignKey('Pensum', on_delete=models.SET_NULL, null=True)
    notas_historicas = models.ManyToManyField('NotaMateria', related_name='estudiantes')

    def __str__(self):
        return f"{self.nombre} - {self.codigo}"

    # Clase Materia
class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50)
    numero_creditos = models.IntegerField()
    primer_prerequisito = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='primer_prereq')
    segundo_prerequisito = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='segundo_prereq')
    tercer_prerequisito = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='tercer_prereq')
    materias_equivalentes = models.ManyToManyField('self', symmetrical=True, blank=True)

    def __str__(self):
        return self.nombre
    

    # Clase Pensum
class Pensum(models.Model):
    materias = models.ManyToManyField(Materia)

    def __str__(self):
        return "Pensum"
    
    
    # Clase Grupo
class Grupo(models.Model):
    nombre = models.CharField(max_length=50)
    semestre = models.CharField(max_length=10)
    horario = models.CharField(max_length=100)
    salon = models.CharField(max_length=50)
    cupo = models.IntegerField()
    estado = models.BooleanField()
    estudiantes = models.ManyToManyField(Estudiante, related_name='grupos')
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre
    
 # Clase Asignacion Docente
class AsignacionDocente(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    periodo_academico = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.docente} - {self.materia}"

# Clase Matricucla
class Matricula(models.Model):
    codigo_materia = models.CharField(max_length=50)
    periodo_academico = models.CharField(max_length=50)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.estudiante} - {self.codigo_materia}"



# Clase Nota Materia
class NotaMateria(models.Model):
    calificacion = models.IntegerField()

    def __str__(self):
        return f"Calificación: {self.calificacion}"


# Clase Calculadora de notas
class CalculadoraNotas(models.Model):
    notas = models.ManyToManyField(NotaMateria)

    def calcular_promedio(self):
        total = sum([nota.calificacion for nota in self.notas.all()])
        cantidad = self.notas.count()
        return total / cantidad if cantidad > 0 else 0



# Clase Notificacion
class Notificacion(models.Model):
    contenido = models.TextField()

    def enviar_notificacion(self):
        # Lógica para enviar la notificación
        pass

    def __str__(self):
        return self.contenido
    
    