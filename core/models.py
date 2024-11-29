# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Calificaciones(models.Model):
    calificacionid = models.AutoField(db_column='CalificacionID', primary_key=True)
    estudianteid = models.ForeignKey('Estudiantes', models.DO_NOTHING, db_column='EstudianteID')
    materiaid = models.ForeignKey('Materias', models.DO_NOTHING, db_column='MateriaID')
    notaparcial = models.FloatField(db_column='NotaParcial')
    notafinal = models.FloatField(db_column='NotaFinal', blank=True, null=True)
    fecharegistro = models.DateTimeField(db_column='FechaRegistro', blank=True, null=True)

    def __str__(self):
        return f"{self.estudianteid.usuarioid.nombre} - {self.materiaid.nombremateria}"

    class Meta:
        managed = False
        db_table = 'Calificaciones'



class Chats(models.Model):
    chatid = models.AutoField(db_column='ChatID', primary_key=True)  # Llave primaria
    usuarioorigenid = models.ForeignKey(
        'Usuarios', models.DO_NOTHING, db_column='UsuarioOrigenID', related_name='chats_enviados'
    )  # Usuario que envía el mensaje
    usuariodestinoid = models.ForeignKey(
        'Usuarios', models.DO_NOTHING, db_column='UsuarioDestinoID', related_name='chats_recibidos'
    )  # Usuario que recibe el mensaje
    mensaje = models.TextField(db_column='Mensaje')  # Contenido del mensaje
    fechaenvio = models.DateTimeField(db_column='FechaEnvio', blank=True, null=True)  # Fecha de envío
    leido = models.BooleanField(db_column='Leido', default=False)  # Estado de lectura

    def __str__(self):
        return f"De: {self.usuarioorigenid.nombre} a {self.usuariodestinoid.nombre}"

    class Meta:
        managed = False
        db_table = 'Chats'


class Deudas(models.Model):
    deudaid = models.AutoField(db_column='DeudaID', primary_key=True)  # Llave primaria
    estudianteid = models.ForeignKey('Estudiantes', models.DO_NOTHING, db_column='EstudianteID')  # Relación con Estudiantes
    concepto = models.CharField(db_column='Concepto', max_length=255)  # Concepto de la deuda
    monto = models.DecimalField(db_column='Monto', max_digits=10, decimal_places=2)  # Monto de la deuda
    estado = models.CharField(db_column='Estado', max_length=9, default='Pendiente')  # Estado de la deuda
    fechageneracion = models.DateTimeField(db_column='FechaGeneracion', blank=True, null=True)  # Fecha de generación

    def __str__(self):
        return f"{self.estudianteid.usuarioid.nombre} - {self.concepto} ({self.estado})"

    class Meta:
        managed = False
        db_table = 'Deudas'


class Docentes(models.Model):
    docenteid = models.AutoField(db_column='DocenteID', primary_key=True)  # Field name made lowercase.
    usuarioid = models.OneToOneField('Usuarios', models.DO_NOTHING, db_column='UsuarioID')  # Field name made lowercase.

    def __str__(self):
        # Devuelve el nombre completo del usuario asociado
        return f"{self.usuarioid.nombre} {self.usuarioid.apellido}"
    
    class Meta:
        managed = False
        db_table = 'Docentes'


class Estudiantes(models.Model):
    estudianteid = models.AutoField(db_column='EstudianteID', primary_key=True)
    usuarioid = models.OneToOneField('Usuarios', models.DO_NOTHING, db_column='UsuarioID')
    programaid = models.ForeignKey('Programasacademicos', models.DO_NOTHING, db_column='ProgramaID', blank=True, null=True)

    def __str__(self):
        # Devuelve el nombre completo del usuario relacionado
        return f"{self.usuarioid.nombre} {self.usuarioid.apellido}"

    class Meta:
        managed = False
        db_table = 'Estudiantes'



class GruposChat(models.Model):
    grupochatid = models.AutoField(db_column='GrupoChatID', primary_key=True)  # Llave primaria
    nombregrupo = models.CharField(db_column='NombreGrupo', max_length=150)  # Nombre del grupo
    fechacreacion = models.DateTimeField(db_column='FechaCreacion', blank=True, null=True)  # Fecha de creación

    def __str__(self):
        return self.nombregrupo

    class Meta:
        managed = False
        db_table = 'GruposChat'


class Horarios(models.Model):
    horarioid = models.AutoField(db_column='HorarioID', primary_key=True)  # Field name made lowercase.
    materiaid = models.ForeignKey('Materias', models.DO_NOTHING, db_column='MateriaID')  # Field name made lowercase.
    docenteid = models.ForeignKey(Docentes, models.DO_NOTHING, db_column='DocenteID')  # Field name made lowercase.
    dia = models.CharField(db_column='Dia', max_length=9)  # Field name made lowercase.
    horainicio = models.TimeField(db_column='HoraInicio')  # Field name made lowercase.
    horafin = models.TimeField(db_column='HoraFin')  # Field name made lowercase.
    aula = models.CharField(db_column='Aula', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f"{self.materiaid.nombremateria} - {self.docenteid.usuarioid.nombre} {self.docenteid.usuarioid.apellido} ({self.dia})"
    
    class Meta:
        managed = False
        db_table = 'Horarios'


class Inscripciones(models.Model):
    inscripcionid = models.AutoField(db_column='InscripcionID', primary_key=True)  # Field name made lowercase.
    estudianteid = models.ForeignKey(Estudiantes, models.DO_NOTHING, db_column='EstudianteID')  # Field name made lowercase.
    materiaid = models.ForeignKey('Materias', models.DO_NOTHING, db_column='MateriaID')  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fechainscripcion = models.DateTimeField(db_column='FechaInscripcion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Inscripciones'


class Logs(models.Model):
    logid = models.AutoField(db_column='LogID', primary_key=True)  # Llave primaria
    usuarioid = models.ForeignKey(
        'Usuarios', models.DO_NOTHING, db_column='UsuarioID'
    )  # Relación con Usuarios
    accion = models.TextField(db_column='Accion')  # Detalle de la acción realizada
    fechaaccion = models.DateTimeField(db_column='FechaAccion', blank=True, null=True)  # Fecha y hora de la acción

    class Meta:
        managed = False
        db_table = 'Logs'





class Materias(models.Model):
    materiaid = models.AutoField(db_column='MateriaID', primary_key=True)
    nombremateria = models.CharField(db_column='NombreMateria', max_length=150)
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)
    creditos = models.IntegerField(db_column='Creditos')
    cuposdisponibles = models.IntegerField(db_column='CuposDisponibles')
    estado = models.CharField(db_column='Estado', max_length=7, blank=True, null=True)
    semestre = models.PositiveSmallIntegerField(  # Nuevo campo para Semestre
        db_column='Semestre',
        validators=[
            MinValueValidator(1, "El semestre debe ser al menos 1."),
            MaxValueValidator(10, "El semestre no puede ser mayor a 10.")
        ]
    )

    def __str__(self):
        return self.nombremateria  # Muestra el nombre de la materia
    
    class Meta:
        managed = False
        db_table = 'Materias'



class Miembrosgrupochat(models.Model):
    miembroid = models.AutoField(db_column='MiembroID', primary_key=True)
    grupochatid = models.ForeignKey(
        'GruposChat', models.DO_NOTHING, db_column='GrupoChatID'
    )
    usuarioid = models.ForeignKey(
        'Usuarios', models.DO_NOTHING, db_column='UsuarioID'
    )

    class Meta:
        managed = False
        db_table = 'MiembrosGrupoChat'


class Notificaciones(models.Model):
    notificacionid = models.AutoField(db_column='NotificacionID', primary_key=True)  # Llave primaria
    usuarioid = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='UsuarioID')  # Relación con Usuarios
    tipo = models.CharField(db_column='Tipo', max_length=14)  # Tipo de notificación
    mensaje = models.TextField(db_column='Mensaje')  # Contenido del mensaje
    leida = models.BooleanField(db_column='Leida', default=False)  # Estado de lectura
    fechaenvio = models.DateTimeField(db_column='FechaEnvio', blank=True, null=True)  # Fecha de envío

    def __str__(self):
        return f"{self.usuarioid.nombre} - {self.tipo}"

    class Meta:
        managed = False
        db_table = 'Notificaciones'


class Pagos(models.Model):
    pagoid = models.AutoField(db_column='PagoID', primary_key=True)  # Llave primaria
    estudianteid = models.ForeignKey('Estudiantes', models.DO_NOTHING, db_column='EstudianteID')  # Relación con Estudiantes
    deudaid = models.ForeignKey('Deudas', models.DO_NOTHING, db_column='DeudaID', blank=True, null=True)  # Relación con Deudas (opcional)
    monto = models.DecimalField(db_column='Monto', max_digits=10, decimal_places=2)  # Monto del pago
    metodopago = models.CharField(db_column='MetodoPago', max_length=13)  # Método de pago
    fechapago = models.DateTimeField(db_column='FechaPago', blank=True, null=True)  # Fecha del pago

    def __str__(self):
        return f"{self.estudianteid.usuarioid.nombre} - {self.monto} ({self.metodopago})"

    class Meta:
        managed = False
        db_table = 'Pagos'


class Pensums(models.Model):
    pensumid = models.AutoField(db_column='PensumID', primary_key=True)  # Field name made lowercase.
    programaid = models.ForeignKey('Programasacademicos', models.DO_NOTHING, db_column='ProgramaID')  # Field name made lowercase.
    materiaid = models.ForeignKey(Materias, models.DO_NOTHING, db_column='MateriaID')  # Field name made lowercase.
    esobligatoria = models.IntegerField(db_column='EsObligatoria')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pensums'


class Prerequisitos(models.Model):
    prerequisitoid = models.AutoField(db_column='PrerequisitoID', primary_key=True)  # Field name made lowercase.
    materiaid = models.ForeignKey(Materias, models.DO_NOTHING, db_column='MateriaID')  # Field name made lowercase.
    materiarequeridaid = models.ForeignKey(Materias, models.DO_NOTHING, db_column='MateriaRequeridaID', related_name='prerequisitos_materiarequeridaid_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Prerequisitos'


class Programasacademicos(models.Model):
    programaid = models.AutoField(db_column='ProgramaID', primary_key=True)  # Field name made lowercase.
    nombreprograma = models.CharField(db_column='NombrePrograma', max_length=150)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    fechacreacion = models.DateTimeField(db_column='FechaCreacion', blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        return self.nombreprograma
    
    class Meta:
        managed = False
        db_table = 'ProgramasAcademicos'


class Usuarios(models.Model):
    usuarioid = models.AutoField(db_column='UsuarioID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=100)  # Field name made lowercase.
    tipodocumento = models.CharField(db_column='TipoDocumento', max_length=9)  # Field name made lowercase.
    numerodocumento = models.CharField(db_column='NumeroDocumento', unique=True, max_length=20)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', unique=True, max_length=150)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=15, blank=True, null=True)  # Field name made lowercase.
    contrasena = models.CharField(db_column='Contrasena', max_length=255)  # Field name made lowercase.
    tipousuario = models.CharField(db_column='TipoUsuario', max_length=13)  # Field name made lowercase.
    autenticaciondospasos = models.IntegerField(db_column='AutenticacionDosPasos', blank=True, null=True)  # Field name made lowercase.
    estadoconexion = models.CharField(db_column='EstadoConexion', max_length=12, blank=True, null=True)  # Field name made lowercase.
    fecharegistro = models.DateTimeField(db_column='FechaRegistro', blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"  # Retorna el nombre completo del usuario
    
    class Meta:
        managed = False
        db_table = 'Usuarios'
