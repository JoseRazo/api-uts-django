from .models import Articulo
from rest_framework import generics, permissions
from .serializers import ArticuloSerializer
from rest_framework.pagination import PageNumberPagination

class ArticuloList(generics.ListAPIView):
    paginator = PageNumberPagination()
    paginator.page_size = 12
    queryset = Articulo.objects.all().order_by('-fecha_evento', 'id')
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