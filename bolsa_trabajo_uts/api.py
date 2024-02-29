from rest_framework import generics
from .models import Vacante
from .serializers import VacanteSerializer

class VacanteListAPIView(generics.ListAPIView):
    queryset = Vacante.objects.filter(activo=True)
    serializer_class = VacanteSerializer

