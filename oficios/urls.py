from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('miformulario', views.mascota_view, name='mascota_view'),
    path('busqueda_productos/', views.busqueda_productos, name='busqueda_productos'),
    path('buscar/', views.buscar, name='buscar'),
]