from django.shortcuts import render, get_object_or_404, redirect
from client.models import Producto
from django.contrib.auth import authenticate, login
from .models import auditoriaProductos
from client.forms import *
from administracion.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def iniciarSesion(request):
    if request.method=='POST':
        form= LoginForm(request,request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/indexAdmin/')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

@login_required
def indexAdmin(request):
    auditoria=auditoriaProductos.objects.all()
    return render(request,"indexAdmin.html",{'auditoria':auditoria})

@login_required
def listarProductos(request):
    productos=Producto.objects.all()

    return render(request,'lista_productos.html',{'productos':productos})

@login_required
def crearProducto(request):
    form = productoForm()
    if request.method=='POST':
        form = productoForm(request.POST,request.FILES)
        if form.is_valid():
            producto_creado=form.save()
            auditoriaProductos.objects.create(accion='Creacion',usuario=request.user,producto_modificado=producto_creado.nombre)
            return redirect('/ListaProductos/')
    return render(request,'crear_producto.html',{'form':form})

@login_required
def crearCategoria(request):
    form= categoriaForm()
    if request.method=='POST':
        form = categoriaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/ListaProductos/')
    return render(request,'crear_categoria.html',{'form':form})

@login_required
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = productoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            nombreProducto=producto.nombre
            form.save()
            auditoriaProductos.objects.create(accion='Modificacion', usuario=request.user, producto_modificado=nombreProducto)
            return redirect('/ListaProductos/')
    else:
        form = productoForm(request.POST, request.FILES, instance=producto)
    return render(request,'actualizarProductos.html',{'form':form})

@login_required       
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    nombreProducto=producto.nombre
    producto.delete()
    auditoriaProductos.objects.create(accion='Eliminacion', usuario=request.user, producto_modificado=nombreProducto)
    return redirect('/ListaProductos/')

@login_required
def sobreNosotros(request):
    form=DescripcionEmpresaForm()
    if request.method=='POST':
        form = DescripcionEmpresaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/indexAdmin/')
    return render(request,'sobreNosotros.html',{'form':form})
