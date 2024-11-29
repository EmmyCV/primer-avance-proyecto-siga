from rest_framework.viewsets import ModelViewSet
from core.models import Docentes
from core.serializers import DocenteSerializer


class DocenteViewSet(ModelViewSet):
    """
    ViewSet para manejar las operaciones CRUD de Docentes.
    """
    queryset = Docentes.objects.all()
    serializer_class = DocenteSerializer
