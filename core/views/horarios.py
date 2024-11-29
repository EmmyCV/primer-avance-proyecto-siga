from rest_framework import viewsets
from core.models import Horarios, Inscripciones, Docentes, Estudiantes
from core.serializers import HorarioSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horarios.objects.all()
    serializer_class = HorarioSerializer

    @action(detail=False, methods=['get'], url_path='horario-estudiante/(?P<estudiante_id>\d+)')
    def horario_estudiante(self, request, estudiante_id=None):
        """
        Devuelve el horario de un estudiante basado en las materias inscritas con estado 'Inscrita'.
        """
        try:
            # Obtener las inscripciones activas (estado='Inscrita') del estudiante
            inscripciones = Inscripciones.objects.filter(estudianteid=estudiante_id, estado='Inscrita')

            # Obtener los IDs de las materias inscritas
            materia_ids = inscripciones.values_list('materiaid', flat=True)

            # Buscar los horarios relacionados con esas materias
            horarios = Horarios.objects.filter(materiaid__in=materia_ids)

            # Construir el JSON con los datos solicitados
            horario_data = []
            for horario in horarios:
                horario_data.append({
                    "materia": horario.materiaid.nombremateria,  # Nombre de la materia
                    "dia": horario.dia,  # Día de la clase
                    "hora_inicio": horario.horainicio,  # Hora de inicio
                    "hora_fin": horario.horafin,  # Hora de fin
                    "aula": horario.aula  # Aula
                })

            return Response(horario_data)

        except Inscripciones.DoesNotExist:
            return Response({"detail": "Estudiante no encontrado o sin inscripciones activas."}, status=404)

from rest_framework import viewsets
from core.models import Horarios, Inscripciones, Docentes, Estudiantes
from core.serializers import HorarioSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horarios.objects.all()
    serializer_class = HorarioSerializer

    @action(detail=False, methods=['get'], url_path='horario-estudiante/(?P<estudiante_id>\d+)')
    def horario_estudiante(self, request, estudiante_id=None):
        """
        Devuelve el horario de un estudiante basado en las materias inscritas con estado 'Inscrita'.
        """
        try:
            inscripciones = Inscripciones.objects.filter(estudianteid=estudiante_id, estado='Inscrita')
            materia_ids = inscripciones.values_list('materiaid', flat=True)
            horarios = Horarios.objects.filter(materiaid__in=materia_ids)

            horario_data = [
                {
                    "materia": horario.materiaid.nombremateria,
                    "dia": horario.dia,
                    "hora_inicio": horario.horainicio,
                    "hora_fin": horario.horafin,
                    "aula": horario.aula,
                }
                for horario in horarios
            ]

            return Response(horario_data)
        except Inscripciones.DoesNotExist:
            return Response({"detail": "Estudiante no encontrado o sin inscripciones activas."}, status=404)

    @action(detail=False, methods=['get'], url_path='materias-docente/(?P<usuario_id>\d+)')
    def materias_docente(self, request, usuario_id=None):
        """
        Devuelve las materias dictadas por un docente basado en su usuarioID junto con la información del curso.
        """
        try:
            # Verificar si existe un docente asociado al usuario
            docente = Docentes.objects.get(usuarioid=usuario_id)

            # Obtener los horarios de las materias dictadas por el docente
            horarios = Horarios.objects.filter(docenteid=docente)

            if not horarios.exists():
                return Response({"detail": "El docente no tiene materias asignadas."}, status=404)

            materias_dictadas = []
            for horario in horarios:
                # Obtener los estudiantes inscritos en la materia
                inscripciones = Inscripciones.objects.filter(
                    materiaid=horario.materiaid, estado='Inscrita'
                )
                estudiantes = [
                    {
                        "estudiante_id": inscripcion.estudianteid.estudianteid,
                        "nombre_completo": f"{inscripcion.estudianteid.usuarioid.nombre} {inscripcion.estudianteid.usuarioid.apellido}",
                    }
                    for inscripcion in inscripciones
                ]

                materias_dictadas.append({
                    "materia_id": horario.materiaid.materiaid,
                    "nombre_materia": horario.materiaid.nombremateria,
                    "horario": {
                        "dia": horario.dia,
                        "hora_inicio": horario.horainicio,
                        "hora_fin": horario.horafin,
                        "aula": horario.aula,
                    },
                    "estudiantes": estudiantes,
                })

            return Response({
                "usuario_id": usuario_id,
                "materias_dictadas": materias_dictadas,
            })

        except Docentes.DoesNotExist:
            return Response({"detail": "Docente no encontrado."}, status=404)
