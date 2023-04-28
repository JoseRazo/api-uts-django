from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .api import InstitucionList, InstitucionDetailView

app_name='becas'

urlpatterns = [
    path('instituciones/', InstitucionList.as_view()),
    path('instituciones/<int:pk>', InstitucionDetailView.as_view()),
]
