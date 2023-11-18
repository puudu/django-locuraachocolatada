from django.shortcuts import render, get_object_or_404, redirect
from client.models import Producto
from .models import auditoriaProductos
from client.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def crearProducto(request):
    form= productosForm()
    if request.method=='POST':
        form = productosForm(request.POST,request.FILES)
        if form.is_valid():
            producto_creado=form.save()
            auditoriaProductos.objects.create(accion='Creacion',usuario=request.user,producto_modificado=producto_creado)
        return redirect('lista_productos.html')
    return render(request,'crear_producto.html',{'form':form})

@login_required
def crearCategoria(request):
    form= categoriaForm()
    if request.method=='POST':
        form = categoriaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('lista_productos.html')
    return render(request,'crear_categoria.html',{'form':form})