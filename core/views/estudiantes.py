from rest_framework.viewsets import ModelViewSet
from core.models import Estudiantes
from core.serializers import EstudianteSerializer


class EstudianteViewSet(ModelViewSet):
    """
    ViewSet para manejar las operaciones CRUD de Estudiantes.
    """
    queryset = Estudiantes.objects.all()
    serializer_class = EstudianteSerializer
