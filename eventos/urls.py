from django.urls import path
from .api import InstructorViewSet,CronogramaViewSet,HotelViewSet,PatrocinadoresViewSet,HeaderViewSet,EventoViewSet,CursoViewSet, Cronograma_Dia2ViewSet


urlpatterns = [
    path('instructores/', InstructorViewSet.as_view()),
    path('cronogramas/', CronogramaViewSet.as_view()),
    path('cronogramas_dia2/', Cronograma_Dia2ViewSet.as_view()),
    path('hoteles/', HotelViewSet.as_view()),
    path('patrocinadores/', PatrocinadoresViewSet.as_view()),
    path('headers/', HeaderViewSet.as_view()),
    path('eventos/', EventoViewSet.as_view()),
    path('cursos/', CursoViewSet.as_view()),
]