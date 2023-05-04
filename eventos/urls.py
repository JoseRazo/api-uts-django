from django.urls import path
from .api import InstructorViewSet,CronogramaViewSet,HotelViewSet,PatrocinadoresViewSet,HeaderViewSet,EventoViewSet


urlpatterns = [
    path('instructores/', InstructorViewSet.as_view()),
    path('cronogramas/', CronogramaViewSet.as_view()),
    path('hoteles/', HotelViewSet.as_view()),
    path('patrocinadores/', PatrocinadoresViewSet.as_view()),
    path('headers/', HeaderViewSet.as_view()),
    path('eventos/',EventoViewSet.as_view()),
]