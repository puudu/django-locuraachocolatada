from django.shortcuts import render
from client.models import *

# Create your views here.
def inicio(request):
    data = descripcionEmpresa.objects.get(id=1)
    productos_promocion = Producto.objects.filter(oferta=True)
    productos_mas_vendidos = Producto.objects.filter(popular=True)
    
    for producto in productos_promocion:
        producto.precio_final = producto.precio
        
        if producto.oferta:
            producto.precio_final = producto.descuento_oferta
            precio_original = producto.precio
            precio_oferta = producto.descuento_oferta

            if precio_original > 0:
                porcentaje_descueto = ((precio_original - precio_oferta) / precio_original) * 100
                producto.porcentaje_descuento = int(round(porcentaje_descueto))
            else:
                producto.porcentaje_descuento = 0
        
    for producto in productos_mas_vendidos:
        producto.precio_final = producto.precio
        
        if producto.oferta:
            producto.precio_final = producto.descuento_oferta
            precio_original = producto.precio
            precio_oferta = producto.descuento_oferta

            if precio_original > 0:
                porcentaje_descueto = ((precio_original - precio_oferta) / precio_original) * 100
                producto.porcentaje_descuento = int(round(porcentaje_descueto))
            else:
                producto.porcentaje_descuento = 0    

    return render(request, 'principal/inicio.html',{'data':data, 'productos_promocion':productos_promocion,'productos_mas_vendidos':productos_mas_vendidos})
    
def productos(request):
    productos = Producto.objects.all()
    data={
        'productos':productos
    }
    return render(request, 'principal/productos.html',data)

def productos_por_categoria(request, categoria_id):
    data = descripcionEmpresa.objects.get(id=1)
    categoria = Categoria.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categoria = categoria)
    categorias = Categoria.objects.all().order_by('id')

    for producto in productos:
        producto.precio_final = producto.precio
        
        if producto.oferta:
            producto.precio_final = producto.descuento_oferta
            precio_original = producto.precio
            precio_oferta = producto.descuento_oferta

            if precio_original > 0:
                porcentaje_descueto = ((precio_original - precio_oferta) / precio_original) * 100
                producto.porcentaje_descuento = int(round(porcentaje_descueto))
            else:
                producto.porcentaje_descuento = 0

    return render(request, 'principal/productos.html', {'productos':productos, 'categorias':categorias, 'categoria_actual':categoria, 'data':data })

def quienes_somos(request):
    data = descripcionEmpresa.objects.get(id=1)
    return render(request, 'principal/quienes_somos.html', {'data':data})

def terminos_y_condiciones(request):
    data = descripcionEmpresa.objects.get(id=1)
    return render(request, 'principal/terminos_y_condiciones.html', {'data':data})

# Configurar view de producto, para ver el detalle del producto segun su id
def producto(request, producto_id):
    data = descripcionEmpresa.objects.get(id=1)
    producto = Producto.objects.get(id=producto_id)

    producto.precio_final = producto.precio
        
    if producto.oferta:
        producto.precio_final = producto.descuento_oferta
        precio_original = producto.precio
        precio_oferta = producto.descuento_oferta
        if precio_original > 0:
            porcentaje_descueto = ((precio_original - precio_oferta) / precio_original) * 100
            producto.porcentaje_descuento = int(round(porcentaje_descueto))
        else:
            producto.porcentaje_descuento = 0

    return render(request, 'principal/producto.html',{'producto':producto, 'data':data})