from rest_framework import serializers
from .models import (
    Usuarios, Programasacademicos, Estudiantes, Docentes, Materias,
    Pensums, Prerequisitos, Inscripciones, Horarios, Calificaciones,
    Deudas, Pagos, Notificaciones, Chats, GruposChat, Miembrosgrupochat, Logs
)


class UsuarioSerializer(serializers.ModelSerializer):
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('Pasaporte', 'Pasaporte')
    ]
    TIPO_USUARIO_CHOICES = [
        ('Estudiante', 'Estudiante'),
        ('Docente', 'Docente'),
        ('Administrador', 'Administrador')
    ]
    ESTADO_CONEXION_CHOICES = [
        ('En línea', 'En línea'),
        ('Desconectado', 'Desconectado')
    ]

    tipodocumento = serializers.ChoiceField(choices=TIPO_DOCUMENTO_CHOICES)
    tipousuario = serializers.ChoiceField(choices=TIPO_USUARIO_CHOICES)
    estadoconexion = serializers.ChoiceField(choices=ESTADO_CONEXION_CHOICES)
    autenticaciondospasos = serializers.BooleanField()  # Convertir entre True/False y 1/0

    class Meta:
        model = Usuarios
        fields = '__all__'



class ProgramaAcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programasacademicos
        fields = '__all__'


class EstudianteSerializer(serializers.ModelSerializer):
    # Mostrar el nombre del programa en lugar del ID
    programaid = serializers.SlugRelatedField(
        queryset=Programasacademicos.objects.all(),  # Para seleccionar programas académicos
        slug_field='nombreprograma'  # Campo que se muestra en lugar del ID
    )
    # Mostrar el nombre completo del usuario en lugar del ID
    usuarioid = serializers.SlugRelatedField(
        queryset=Usuarios.objects.all(),  # Para seleccionar usuarios
        slug_field='nombre'  # Muestra el nombre del usuario
    )

    class Meta:
        model = Estudiantes
        fields = '__all__'



class DocenteSerializer(serializers.ModelSerializer):
    # Mostrar el nombre completo del usuario en lugar del ID
    usuarioid = serializers.SlugRelatedField(
        queryset=Usuarios.objects.all(),  # Para seleccionar usuarios
        slug_field='nombre'  # Muestra el campo 'nombre' del modelo Usuarios
    )

    class Meta:
        model = Docentes
        fields = '__all__'



class MateriaSerializer(serializers.ModelSerializer):
    ESTADO_CHOICES = [
        ('Abierta', 'Abierta'),
        ('Cerrada', 'Cerrada')
    ]
    estado = serializers.ChoiceField(choices=ESTADO_CHOICES)

    class Meta:
        model = Materias
        fields = '__all__'



class PensumSerializer(serializers.ModelSerializer):
    # Mostrar el nombre del programa en lugar del ID
    programaid = serializers.SlugRelatedField(
        queryset=Programasacademicos.objects.all(),
        slug_field='nombreprograma'  # Campo que muestra el nombre del programa
    )
    # Mostrar el nombre de la materia en lugar del ID
    materiaid = serializers.SlugRelatedField(
        queryset=Materias.objects.all(),
        slug_field='nombremateria'  # Campo válido del modelo Materias
    )

    esobligatoria = serializers.BooleanField()
     
    class Meta:
        model = Pensums
        fields = '__all__'



class PrerequisitoSerializer(serializers.ModelSerializer):
    # Mostrar el nombre de la materia en lugar del ID
    materiaid = serializers.SlugRelatedField(
        queryset=Materias.objects.all(),
        slug_field='nombremateria'  # Campo que muestra el nombre de la materia
    )
    # Mostrar el nombre de la materia requerida en lugar del ID
    materiarequeridaid = serializers.SlugRelatedField(
        queryset=Materias.objects.all(),
        slug_field='nombremateria'  # Campo que muestra el nombre de la materia requerida
    )

    class Meta:
        model = Prerequisitos
        fields = '__all__'


class InscripcionSerializer(serializers.ModelSerializer):
    estudianteid = serializers.PrimaryKeyRelatedField(
        queryset=Estudiantes.objects.all()  # Permite seleccionar un estudiante por su ID
    )
    estudiante_nombre = serializers.SerializerMethodField()  # Campo adicional para mostrar el nombre completo
    materiaid = serializers.SlugRelatedField(
        queryset=Materias.objects.all(),
        slug_field='nombremateria'  # Muestra el nombre de la materia
    )
    ESTADO_CHOICES = [
        ('Inscrita', 'Inscrita'),
        ('Homologada', 'Homologada'),
        ('Retirada', 'Retirada')
    ]
    estado = serializers.ChoiceField(choices=ESTADO_CHOICES)

    def get_estudiante_nombre(self, obj):
        """
        Devuelve el nombre completo del estudiante.
        """
        return f"{obj.estudianteid.usuarioid.nombre} {obj.estudianteid.usuarioid.apellido}"

    class Meta:
        model = Inscripciones
        fields = '__all__'

    estudianteid = serializers.PrimaryKeyRelatedField(
        queryset=Estudiantes.objects.all()  # Permite seleccionar un estudiante por su ID
    )
    estudiante_nombre = serializers.SerializerMethodField()  # Campo adicional para mostrar el nombre completo
    materiaid = serializers.SlugRelatedField(
        queryset=Materias.objects.all(),
        slug_field='nombremateria'  # Muestra el nombre de la materia
    )
    ESTADO_CHOICES = [
        ('Inscrita', 'Inscrita'),
        ('Homologada', 'Homologada'),
        ('Retirada', 'Retirada')
    ]
    estado = serializers.ChoiceField(choices=ESTADO_CHOICES)

    def get_estudiante_nombre(self, obj):
        """
        Devuelve el nombre completo del estudiante.
        """
        return f"{obj.estudianteid.usuarioid.nombre} {obj.estudianteid.usuarioid.apellido}"

    class Meta:
        model = Inscripciones
        fields = '__all__'
        extra_fields = ['estudiante_nombre']


class HorarioSerializer(serializers.ModelSerializer):
    materiaid = serializers.SlugRelatedField(
        queryset=Materias.objects.all(),
        slug_field='nombremateria'  # Mostrar el nombre de la materia
    )
    docenteid = serializers.PrimaryKeyRelatedField(
        queryset=Docentes.objects.all()  # Permitir seleccionar un docente por su ID
    )
    docente_nombre = serializers.SerializerMethodField()  # Mostrar el nombre completo del docente
    DIA_CHOICES = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado')
    ]
    dia = serializers.ChoiceField(choices=DIA_CHOICES)  # Días de la semana

    def get_docente_nombre(self, obj):
        """
        Devuelve el nombre completo del docente asociado.
        """
        return f"{obj.docenteid.usuarioid.nombre} {obj.docenteid.usuarioid.apellido}"

    class Meta:
        model = Horarios
        fields = '__all__'


class CalificacionSerializer(serializers.ModelSerializer):
    estudianteid = serializers.PrimaryKeyRelatedField(
        queryset=Estudiantes.objects.all(),
    )
    estudiante_nombre = serializers.SerializerMethodField()
    materiaid = serializers.SlugRelatedField(
        queryset=Materias.objects.all(),
        slug_field='nombremateria'
    )

    def get_estudiante_nombre(self, obj):
        return f"{obj.estudianteid.usuarioid.nombre} {obj.estudianteid.usuarioid.apellido}"

    def validate_notaparcial(self, value):
        if not isinstance(value, float):
            raise serializers.ValidationError("La nota parcial debe ser un número flotante.")
        if value < 0 or value > 5:
            raise serializers.ValidationError("La nota parcial debe estar entre 0 y 5.")
        return value

    def validate_notafinal(self, value):
        if value is not None:
            if not isinstance(value, float):
                raise serializers.ValidationError("La nota final debe ser un número flotante.")
            if value < 0 or value > 5:
                raise serializers.ValidationError("La nota final debe estar entre 0 y 5.")
        return value

    class Meta:
        model = Calificaciones
        fields = '__all__'


class DeudaSerializer(serializers.ModelSerializer):
    estudianteid = serializers.PrimaryKeyRelatedField(
        queryset=Estudiantes.objects.all(),  # Permitir seleccionar un estudiante por su ID
    )
    estudiante_nombre = serializers.SerializerMethodField()  # Muestra el nombre completo del estudiante
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Pagada', 'Pagada')
    ]
    estado = serializers.ChoiceField(choices=ESTADO_CHOICES)  # Estado de la deuda

    def get_estudiante_nombre(self, obj):
        """
        Devuelve el nombre completo del estudiante asociado.
        """
        return f"{obj.estudianteid.usuarioid.nombre} {obj.estudianteid.usuarioid.apellido}"

    class Meta:
        model = Deudas
        fields = '__all__'
        extra_fields = ['estudiante_nombre']

class PagoSerializer(serializers.ModelSerializer):
    estudianteid = serializers.PrimaryKeyRelatedField(
        queryset=Estudiantes.objects.all(),
    )
    estudiante_nombre = serializers.SerializerMethodField()
    deudaid = serializers.PrimaryKeyRelatedField(
        queryset=Deudas.objects.all(),
        required=False,
    )
    deuda_concepto = serializers.SerializerMethodField()
    METODO_PAGO_CHOICES = [
        ('Efectivo', 'Efectivo'),
        ('Tarjeta', 'Tarjeta'),
        ('Transferencia', 'Transferencia'),
    ]
    metodopago = serializers.ChoiceField(choices=METODO_PAGO_CHOICES)

    def get_estudiante_nombre(self, obj):
        return f"{obj.estudianteid.usuarioid.nombre} {obj.estudianteid.usuarioid.apellido}"

    def get_deuda_concepto(self, obj):
        return obj.deudaid.concepto if obj.deudaid else None

    def validate_monto(self, value):
        if value <= 0:
            raise serializers.ValidationError("El monto debe ser un número positivo.")
        return value

    def create(self, validated_data):
        # Crear el pago
        pago = super().create(validated_data)

        # Actualizar el estado de la deuda si el monto coincide
        deuda = validated_data.get('deudaid')
        if deuda and deuda.monto == validated_data['monto']:
            deuda.estado = 'Pagada'
            deuda.save()

        return pago

    class Meta:
        model = Pagos
        fields = '__all__'
        extra_fields = ['estudiante_nombre', 'deuda_concepto']

class NotificacionSerializer(serializers.ModelSerializer):
    usuarioid = serializers.PrimaryKeyRelatedField(
        queryset=Usuarios.objects.all(),  # Permite seleccionar un usuario por su ID
    )
    usuario_nombre = serializers.SerializerMethodField()  # Mostrar el nombre completo del usuario
    TIPO_CHOICES = [
        ('Academica', 'Academica'),
        ('Administrativa', 'Administrativa')
    ]
    tipo = serializers.ChoiceField(choices=TIPO_CHOICES)  # Tipo de notificación

    def get_usuario_nombre(self, obj):
        """
        Devuelve el nombre completo del usuario asociado.
        """
        return f"{obj.usuarioid.nombre} {obj.usuarioid.apellido}"

    class Meta:
        model = Notificaciones
        fields = '__all__'
        extra_fields = ['usuario_nombre']


class ChatSerializer(serializers.ModelSerializer):
    usuarioorigenid = serializers.PrimaryKeyRelatedField(
        queryset=Usuarios.objects.all(),  # Permite seleccionar el usuario origen
    )
    usuarioorigen_nombre = serializers.SerializerMethodField()  # Mostrar el nombre del usuario origen
    usuariodestinoid = serializers.PrimaryKeyRelatedField(
        queryset=Usuarios.objects.all(),  # Permite seleccionar el usuario destino
    )
    usuariodestino_nombre = serializers.SerializerMethodField()  # Mostrar el nombre del usuario destino

    def get_usuarioorigen_nombre(self, obj):
        """
        Devuelve el nombre completo del usuario origen.
        """
        return f"{obj.usuarioorigenid.nombre} {obj.usuarioorigenid.apellido}"

    def get_usuariodestino_nombre(self, obj):
        """
        Devuelve el nombre completo del usuario destino.
        """
        return f"{obj.usuariodestinoid.nombre} {obj.usuariodestinoid.apellido}"

    class Meta:
        model = Chats
        fields = '__all__'
        extra_fields = ['usuarioorigen_nombre', 'usuariodestino_nombre']


class GrupoChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GruposChat
        fields = '__all__'


class MiembroGrupoChatSerializer(serializers.ModelSerializer):
    grupochatid = serializers.SlugRelatedField(
        queryset=GruposChat.objects.all(),  # Permitir seleccionar un grupo
        slug_field='nombregrupo'  # Mostrar el nombre del grupo
    )
    usuarioid = serializers.SlugRelatedField(
        queryset=Usuarios.objects.all(),  # Permitir seleccionar un usuario
        slug_field='nombre'  # Mostrar el nombre del usuario
    )

    class Meta:
        model = Miembrosgrupochat
        fields = '__all__'


class LogSerializer(serializers.ModelSerializer):
    usuarioid = serializers.SlugRelatedField(
        queryset=Usuarios.objects.all(),  # Permitir seleccionar un usuario
        slug_field='nombre'  # Mostrar el nombre del usuario
    )

    class Meta:
        model = Logs
        fields = '__all__'

