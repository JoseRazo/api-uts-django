from rest_framework import generics, permissions
from .models import CarouselItem
from .serializers import CarouselItemSerializer

class CarouselPrincipalListView(generics.ListAPIView):
    queryset = CarouselItem.objects.filter(carousel__nombre="Principal", activo=True)
    serializer_class = CarouselItemSerializer
    permission_classes = [permissions.AllowAny]
