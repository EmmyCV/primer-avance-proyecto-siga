from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import Calificaciones, Estudiantes, Materias
from rest_framework import viewsets
from core.serializers import CalificacionSerializer

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificaciones.objects.all()
    serializer_class = CalificacionSerializer

    @action(detail=False, methods=['get'], url_path='historico-estudiante/(?P<estudiante_id>\d+)')
    def historico_estudiante(self, request, estudiante_id=None):
        """
        Devuelve el registro histórico de notas del estudiante.
        """
        try:
            # Verificar si el estudiante existe
            estudiante = Estudiantes.objects.get(estudianteid=estudiante_id)

            # Obtener las calificaciones del estudiante
            calificaciones = Calificaciones.objects.filter(estudianteid=estudiante)

            # Construir la respuesta con los datos necesarios
            historico_notas = []
            for calificacion in calificaciones:
                historico_notas.append({
                    "materia_id": calificacion.materiaid.materiaid,
                    "nombre_materia": calificacion.materiaid.nombremateria,
                    "nota_parcial": calificacion.notaparcial,
                    "nota_final": calificacion.notafinal,
                    "fecha_registro": calificacion.fecharegistro
                })

            return Response({
                "estudiante_id": estudiante_id,
                "historico_notas": historico_notas
            })

        except Estudiantes.DoesNotExist:
            return Response({"detail": "Estudiante no encontrado."}, status=404)
