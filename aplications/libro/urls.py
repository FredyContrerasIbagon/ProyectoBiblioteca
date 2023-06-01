
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('libros/', views.listlibros.as_view(), name='libros'),
    path('libros-2/', views.listlibros2.as_view(), name='libros-2'),
    path('libros-trg/', views.listlibrosTrg.as_view(), name='libros-trg'),
    path('libro-detalle/<pk>/', views.LibroDetailView.as_view(), name="libro-detalle"),
    path('busqueda_productos/', views.busqueda_productos),
    path('buscar/', views.buscar),
]

