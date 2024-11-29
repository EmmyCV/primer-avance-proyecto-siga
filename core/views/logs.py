from rest_framework import viewsets
from core.models import Logs
from core.serializers import LogSerializer

class LogViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar las operaciones CRUD de Logs.
    """
    queryset = Logs.objects.all()
    serializer_class = LogSerializer
