from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from .api import ArticuloList, ArticuloDetailView, UltimosArticulosList, ArticulosDestacadosList

app_name='noticias'

urlpatterns = [
    path('articulos/', ArticuloList.as_view()),
    path('articulos/<slug>', ArticuloDetailView.as_view()),
    path('ultimos-articulos/', UltimosArticulosList.as_view()),
    path('articulos-destacados/', ArticulosDestacadosList.as_view()),
]
