from rest_framework import generics
from .models import Vacante
from .serializers import VacanteSerializer

class VacanteListAPIView(generics.ListAPIView):
    queryset = Vacante.objects.filter(activo=True).order_by('-fecha_creacion')
    serializer_class = VacanteSerializer

