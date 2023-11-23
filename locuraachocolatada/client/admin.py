from django.contrib import admin
from client.models import *

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'oferta', 'descuento_oferta', 'categoria', 'popular')
    list_filter = ('categoria', 'oferta', 'popular')

class DescripcionEmpresaAdmin(admin.ModelAdmin):
    pass

# Registrar los modelos
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(descripcionEmpresa, DescripcionEmpresaAdmin)