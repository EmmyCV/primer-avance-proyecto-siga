from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from core.models import Usuarios, Docentes, Estudiantes
from core.serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer

    @action(detail=False, methods=['get'], url_path='tipo-usuario/(?P<usuario_id>\d+)')
    def tipo_usuario(self, request, usuario_id=None):
        """
        Devuelve si un usuario es docente, estudiante, o ninguno.
        """
        try:
            usuario = Usuarios.objects.get(usuarioid=usuario_id)

            # Verificar si el usuario es estudiante
            if Estudiantes.objects.filter(usuarioid=usuario).exists():
                return Response({
                    "usuario_id": usuario_id,
                    "tipo": "Estudiante"
                })

            # Verificar si el usuario es docente
            if Docentes.objects.filter(usuarioid=usuario).exists():
                return Response({
                    "usuario_id": usuario_id,
                    "tipo": "Docente"
                })

            # Si no es ni estudiante ni docente
            return Response({
                "usuario_id": usuario_id,
                "tipo": "Ninguno"
            })

        except Usuarios.DoesNotExist:
            return Response({"detail": "Usuario no encontrado."}, status=404)
