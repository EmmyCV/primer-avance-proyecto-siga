from rest_framework.viewsets import ModelViewSet
from core.models import Programasacademicos
from core.serializers import ProgramaAcademicoSerializer


class ProgramaAcademicoViewSet(ModelViewSet):
    """
    ViewSet para manejar las operaciones CRUD de Programas Académicos.
    """
    queryset = Programasacademicos.objects.all()
    serializer_class = ProgramaAcademicoSerializer
