from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import Materias, Inscripciones, Prerequisitos, Estudiantes
from rest_framework import viewsets
from core.serializers import MateriaSerializer

class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materias.objects.all()
    serializer_class = MateriaSerializer

    @action(detail=False, methods=['get'], url_path='materias-disponibles/(?P<estudiante_id>\d+)')
    def materias_disponibles(self, request, estudiante_id=None):
        """
        Devuelve las materias disponibles para un estudiante basado en:
        - Cupos disponibles.
        - Estado 'Abierta'.
        - Cumplimiento de los requisitos previos.
        """
        try:
            # Obtener al estudiante
            estudiante = Estudiantes.objects.get(estudianteid=estudiante_id)

            # Materias ya inscritas o aprobadas por el estudiante
            materias_inscritas = Inscripciones.objects.filter(
                estudianteid=estudiante, estado='Inscrita'
            ).values_list('materiaid', flat=True)

            materias_aprobadas = Inscripciones.objects.filter(
                estudianteid=estudiante, estado='Homologada'
            ).values_list('materiaid', flat=True)

            # Combinar ambas listas
            materias_no_disponibles = set(materias_inscritas).union(set(materias_aprobadas))

            # Verificar requisitos previos
            materias_disponibles = []
            todas_materias = Materias.objects.filter(estado='Abierta', cuposdisponibles__gt=0)

            for materia in todas_materias:
                # Obtener los requisitos previos de la materia
                requisitos = Prerequisitos.objects.filter(materiaid=materia).values_list('materiarequeridaid', flat=True)
                if all(req in materias_aprobadas for req in requisitos) and materia.materiaid not in materias_no_disponibles:
                    materias_disponibles.append({
                        "materia_id": materia.materiaid,
                        "nombre_materia": materia.nombremateria,
                        "creditos": materia.creditos,
                        "cupos_disponibles": materia.cuposdisponibles,
                        "estado": materia.estado
                    })

            return Response({
                "estudiante_id": estudiante_id,
                "materias_disponibles": materias_disponibles
            })

        except Estudiantes.DoesNotExist:
            return Response({"detail": "Estudiante no encontrado."}, status=404)
