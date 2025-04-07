from django.urls import path
from .api import VacanteListAPIView

app_name='bolsa_trabajo_uts'

urlpatterns = [
    path('vacantes/', VacanteListAPIView.as_view()),
]