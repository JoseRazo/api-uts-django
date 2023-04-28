from django.urls import path
from .api import InstructorViewSet,CronogramaViewSet,HotelViewSet,PatrocinadoresViewSet,HeaderViewSet,EventoViewSet


urlpatterns = [
    path('instructores/', InstructorViewSet.as_view()),
]