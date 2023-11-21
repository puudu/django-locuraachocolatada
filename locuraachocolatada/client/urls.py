from django.urls import path 
from . import views
from administracion import views as admin

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('quienes-somos/', views.quienes_somos, name='quienes-somos'),
    path('terminos-y-condiciones/', views.terminos_y_condiciones, name='terminos-y-condiciones'),
    path('producto/<int:producto_id>/', views.producto, name="producto"),

    # estas urls deberias llevarlas a un views.py dentro de el app administracion
    # y darles otro path, algo como 'admin/crear_producto' mas que nada por un tema de orden
    path('crear_producto/', admin.crearProducto , name="addProducto"),
    path('crear_categoria/', admin.crearCategoria , name="addCategoria"),


]