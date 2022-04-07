from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='inicio'),
    path('registrarcurso/', views.registrarcurso, name='registrando'),
    path('eliminacionCurso/<codigo>', views.eliminacionCurso, name='eliminiar'),
    path('edicionCurso/<codigo>', views.edicionCurso, name='editar'),
    path('editarCurso/', views.editarCurso, name='cursoeditado'),
]