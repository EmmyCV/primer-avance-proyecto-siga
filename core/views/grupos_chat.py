from rest_framework import viewsets
from core.models import GruposChat
from core.serializers import GrupoChatSerializer

class GrupoChatViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar las operaciones CRUD de GruposChat.
    """
    queryset = GruposChat.objects.all()
    serializer_class = GrupoChatSerializer
