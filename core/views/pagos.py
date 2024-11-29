from rest_framework import viewsets
from core.models import Pagos
from core.serializers import PagoSerializer

class PagoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar las operaciones CRUD de Pagos.
    """
    queryset = Pagos.objects.all()
    serializer_class = PagoSerializer
