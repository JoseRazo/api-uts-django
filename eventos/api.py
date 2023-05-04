from .models import Instructor,Cronograma,Hotel,Patrocinadores,Header,Evento
from rest_framework import viewsets, permissions, generics
from .serializers import InstructorSerializer,CronogramaSerializer,HotelSerializer,PatrocinadoresSerializer,HeaderSerializer,EventoSerializer

class InstructorViewSet(generics.ListAPIView):
    queryset = Instructor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InstructorSerializer

class CronogramaViewSet(generics.ListAPIView):
    queryset = Cronograma.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CronogramaSerializer

class HotelViewSet(generics.ListAPIView):
    queryset = Hotel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = HotelSerializer

class PatrocinadoresViewSet(generics.ListAPIView):
    queryset = Patrocinadores.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PatrocinadoresSerializer

class HeaderViewSet(generics.ListAPIView):
    queryset = Header.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = HeaderSerializer

class EventoViewSet(generics.ListAPIView):
    queryset = Evento.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EventoSerializer