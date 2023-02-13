from .models import Articulo
from rest_framework import generics, permissions
from .serializers import ArticuloSerializer

class ArticuloList(generics.ListAPIView):
    queryset = Articulo.objects.all().order_by('-fecha_evento')
    serializer_class = ArticuloSerializer
    permission_classes = [permissions.AllowAny]

class ArticuloDetailView(generics.RetrieveAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    lookup_field = 'slug'

class UltimosArticulosList(generics.ListAPIView):
    queryset = Articulo.objects.all().order_by('-fecha_evento')[:3]
    serializer_class = ArticuloSerializer

class ArticulosDestacadosList(generics.ListAPIView):
    queryset = Articulo.objects.order_by('?')[:3]
    serializer_class = ArticuloSerializer