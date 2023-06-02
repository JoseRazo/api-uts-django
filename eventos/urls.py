from django.urls import path
from .api import InstructorViewSet,CronogramaViewSet,HotelViewSet,PatrocinadoresViewSet,HeaderViewSet,EventoViewSet,CursoViewSet
from .views import EnviarFormularioAPI, RegistroAPI
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('instructores/', InstructorViewSet.as_view()),
    path('cronogramas/', CronogramaViewSet.as_view()),
    path('hoteles/', HotelViewSet.as_view()),
    path('patrocinadores/', PatrocinadoresViewSet.as_view()),
    path('headers/', HeaderViewSet.as_view()),
    path('eventos/', EventoViewSet.as_view()),
    path('cursos/', CursoViewSet.as_view()),
    path('enviar-formulario/', EnviarFormularioAPI.as_view(), name='enviar-formulario'),
    path('registro/', RegistroAPI.as_view(), name='registro'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)