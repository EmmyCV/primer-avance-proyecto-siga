from rest_framework import viewsets
from core.models import Miembrosgrupochat
from core.serializers import MiembroGrupoChatSerializer

class MiembroGrupoChatViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar las operaciones CRUD de MiembrosGrupoChat.
    """
    queryset = Miembrosgrupochat.objects.all()
    serializer_class = MiembroGrupoChatSerializer
