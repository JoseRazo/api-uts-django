from rest_framework import generics
from .models import Departamento
from .serializers import DepartamentoSerializer

class DepartamentoListAPIView(generics.ListAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
