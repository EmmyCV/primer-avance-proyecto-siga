from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import Deudas, Estudiantes
from core.serializers import DeudaSerializer
from rest_framework import viewsets

class DeudaViewSet(viewsets.ModelViewSet):
    queryset = Deudas.objects.all()
    serializer_class = DeudaSerializer

    @action(detail=False, methods=['get'], url_path='deudas-estudiante/(?P<estudiante_id>\d+)')
    def deudas_estudiante(self, request, estudiante_id=None):
        """
        Devuelve las deudas del estudiante.
        """
        try:
            # Verificar si el estudiante existe
            estudiante = Estudiantes.objects.get(estudianteid=estudiante_id)

            # Obtener las deudas del estudiante
            deudas = Deudas.objects.filter(estudianteid=estudiante)

            # Construir la respuesta con los datos necesarios
            lista_deudas = []
            for deuda in deudas:
                lista_deudas.append({
                    "deuda_id": deuda.deudaid,
                    "concepto": deuda.concepto,
                    "monto": deuda.monto,
                    "estado": deuda.estado,
                    "fecha_generacion": deuda.fechageneracion
                })

            return Response({
                "estudiante_id": estudiante_id,
                "deudas": lista_deudas
            })

        except Estudiantes.DoesNotExist:
            return Response({"detail": "Estudiante no encontrado."}, status=404)
