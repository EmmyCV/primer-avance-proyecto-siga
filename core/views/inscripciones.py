from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import Inscripciones, Estudiantes, Materias
from core.serializers import InscripcionSerializer

class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripciones.objects.all()
    serializer_class = InscripcionSerializer

    @action(detail=False, methods=['get'], url_path='materias-estudiante/(?P<estudiante_id>\d+)')
    def materias_estudiante(self, request, estudiante_id=None):
        """
        Devuelve las materias matriculadas de un estudiante basado en su ID.
        """
        try:
            # Obtener las inscripciones del estudiante
            inscripciones = Inscripciones.objects.filter(estudianteid=estudiante_id, estado='Inscrita')

            # Construir la respuesta con las materias matriculadas
            materias_matriculadas = []
            for inscripcion in inscripciones:
                materias_matriculadas.append({
                    "materia_id": inscripcion.materiaid.materiaid,
                    "nombre_materia": inscripcion.materiaid.nombremateria,
                    "creditos": inscripcion.materiaid.creditos,
                    "estado": inscripcion.estado,
                    "fecha_inscripcion": inscripcion.fechainscripcion
                })

            return Response({
                "estudiante_id": estudiante_id,
                "materias_matriculadas": materias_matriculadas
            })

        except Estudiantes.DoesNotExist:
            return Response({"detail": "Estudiante no encontrado."}, status=404)
