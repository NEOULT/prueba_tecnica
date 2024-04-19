from django.urls import path
from .import views

urlpatterns = [

    path('', views.home),
    path('registrarMateria/',views.registrarMateria),
    path('eliminarMateria/<codigo>',views.eliminarMateria),
    path('edicionMateria/<codigo>',views.edicionMateria),
    path('editarMateria/',views.editarMateria),
    path('buscarMateria/<codigo>',views.buscarMateria),
    path('mostrarMateria/',views.mostrarMateria),
]
