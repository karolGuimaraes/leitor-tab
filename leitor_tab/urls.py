from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('importar', views.importar_arquivo, name='importar_arquivo'),
]