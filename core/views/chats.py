from rest_framework import viewsets
from core.models import Chats
from core.serializers import ChatSerializer

class ChatViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar las operaciones CRUD de Chats.
    """
    queryset = Chats.objects.all()
    serializer_class = ChatSerializer
