from django.urls import path 
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.productos, name='productos'),
    path('quienes-somos/', views.quienes_somos, name='quienes-somos'),
    path('terminos-y-condiciones/', views.terminos_y_condiciones, name='terminos-y-condiciones'),
    # Configurar url de producto, para ver el detalle del producto segun su id
    path('producto/', views.producto, name="producto")
]