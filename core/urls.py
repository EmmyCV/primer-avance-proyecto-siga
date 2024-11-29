from rest_framework.routers import DefaultRouter
from core.views.usuarios import UsuarioViewSet
from core.views.programas_academicos import ProgramaAcademicoViewSet
from core.views.estudiantes import EstudianteViewSet
from core.views.docentes import DocenteViewSet
from core.views.materias import MateriaViewSet
from core.views.pensums import PensumViewSet
from core.views.prerequisitos import PrerequisitoViewSet
from core.views.inscripciones import InscripcionViewSet
from core.views.horarios import HorarioViewSet
from core.views.calificaciones import CalificacionViewSet
from core.views.deudas import DeudaViewSet
from core.views.pagos import PagoViewSet
from core.views.notificaciones import NotificacionViewSet
from core.views.chats import ChatViewSet
from core.views.grupos_chat import GrupoChatViewSet
from core.views.miembros_grupo_chat import MiembroGrupoChatViewSet
from core.views.logs import LogViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'programas-academicos', ProgramaAcademicoViewSet, basename='programas-academicos')
router.register(r'estudiantes', EstudianteViewSet, basename='estudiantes')
router.register(r'docentes', DocenteViewSet, basename='docentes')
router.register(r'materias', MateriaViewSet, basename='materias')
router.register(r'pensums', PensumViewSet, basename='pensums')
router.register(r'prerequisitos', PrerequisitoViewSet, basename='prerequisitos')
router.register(r'inscripciones', InscripcionViewSet, basename='inscripciones')
router.register(r'horarios', HorarioViewSet, basename='horarios')
router.register(r'calificaciones', CalificacionViewSet, basename='calificaciones')
router.register(r'deudas', DeudaViewSet, basename='deudas')
router.register(r'pagos', PagoViewSet, basename='pagos')
router.register(r'notificaciones', NotificacionViewSet, basename='notificaciones')
router.register(r'chats', ChatViewSet, basename='chats')
router.register(r'grupos_chat', GrupoChatViewSet, basename='grupos_chat')
router.register(r'miembros_grupo_chat', MiembroGrupoChatViewSet, basename='miembros_grupo_chat')
router.register(r'logs', LogViewSet, basename='logs')

urlpatterns = router.urls
