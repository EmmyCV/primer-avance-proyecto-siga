from rest_framework.viewsets import ModelViewSet
from core.models import Prerequisitos
from core.serializers import PrerequisitoSerializer


class PrerequisitoViewSet(ModelViewSet):
    """
    ViewSet para manejar las operaciones CRUD de Prerequisitos.
    """
    queryset = Prerequisitos.objects.all()
    serializer_class = PrerequisitoSerializer
