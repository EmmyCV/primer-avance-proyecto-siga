from rest_framework import viewsets
from core.models import Notificaciones
from core.serializers import NotificacionSerializer

class NotificacionViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar las operaciones CRUD de Notificaciones.
    """
    queryset = Notificaciones.objects.all()
    serializer_class = NotificacionSerializer
