from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import Pensums, Estudiantes, Materias
from core.serializers import PensumSerializer

class PensumViewSet(viewsets.ModelViewSet):
    queryset = Pensums.objects.all()
    serializer_class = PensumSerializer

    @action(detail=False, methods=['get'], url_path='pensum-estudiante/(?P<estudiante_id>\d+)')
    def pensum_estudiante(self, request, estudiante_id=None):
        """
        Devuelve el pénsum académico de un estudiante, separando materias obligatorias y electivas.
        """
        try:
            # Obtener el estudiante y su programa académico
            estudiante = Estudiantes.objects.get(estudianteid=estudiante_id)
            programa_id = estudiante.programaid.programaid

            # Consultar el pénsum del programa
            pensum = Pensums.objects.filter(programaid=programa_id)

            # Separar materias obligatorias y electivas
            obligatorias = pensum.filter(esobligatoria=True).values(
                'materiaid__materiaid', 
                'materiaid__nombremateria',
                'materiaid__creditos'
            )
            electivas = pensum.filter(esobligatoria=False).values(
                'materiaid__materiaid', 
                'materiaid__nombremateria',
                'materiaid__creditos'
            )

            # Construir la respuesta
            data = {
                "estudiante_id": estudiante_id,
                "programa_id": programa_id,
                "materias_obligatorias": list(obligatorias),
                "materias_electivas": list(electivas)
            }

            return Response(data)

        except Estudiantes.DoesNotExist:
            return Response({"detail": "Estudiante no encontrado."}, status=404)
        except Pensums.DoesNotExist:
            return Response({"detail": "No se encontraron materias para el programa del estudiante."}, status=404)
