from django.conf import settings
from django.urls import path, include, re_path
from django.views.static import serve
from . import views
from administracion import views as admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('quienes-somos/', views.quienes_somos, name='quienes-somos'),
    path('terminos-y-condiciones/', views.terminos_y_condiciones, name='terminos-y-condiciones'),
    path('producto/<int:producto_id>/', views.producto, name="producto"),

    # estas urls deberias llevarlas a un views.py dentro de el app administracion
    # y darles otro path, algo como 'admin/crear_producto' mas que nada por un tema de orden
    path('Login/',admin.iniciarSesion),
    path('indexAdmin/', admin.indexAdmin, name='indexAdmin'),
    path('ListaProductos/',admin.listarProductos,name='ListaProductos'),
    path('Logout/', auth_views.LogoutView.as_view(), name='Logout'),
    path('addProducto/', admin.crearProducto , name="addProducto"),
    path('addCategoria/', admin.crearCategoria , name="addCategoria"),
    path('eliminarProducto/<int:id>',admin.eliminar_producto,name='eliminarProducto'),
    path('modificarProducto/<int:id>',admin.editar_producto,name='modificarProducto'),
    path('actualizarProductos/<int:id>',admin.editar_producto,name='acualizarProductos'),
    path('sobreNosotros/',admin.sobreNosotros,name='sobreNosotros')


]
if settings.DEBUG:
    urlpatterns += [re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT,})]