from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .api import CarouselPrincipalListView

app_name='widgets'
urlpatterns = [
    path('carousel-principal/', CarouselPrincipalListView.as_view()),
]
