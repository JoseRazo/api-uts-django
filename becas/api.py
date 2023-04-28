from .models import Institucion
from rest_framework import generics, permissions
from .serializers import InstitucionSerializer
from rest_framework.pagination import PageNumberPagination

class InstitucionList(generics.ListAPIView):
    queryset = Institucion.objects.all().order_by('nombre')
    serializer_class = InstitucionSerializer
    permission_classes = [permissions.AllowAny]

class InstitucionDetailView(generics.RetrieveAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer
