
from django.urls import path
from .api import DepartamentoListAPIView

app_name='sgc'

urlpatterns = [
    path('sgc/documentos/', DepartamentoListAPIView.as_view()),
]

