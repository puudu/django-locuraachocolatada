from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'principal/inicio.html')
    
def productos(request):
    return render(request, 'principal/productos.html')

def quienes_somos(request):
    return render(request, 'principal/quienes_somos.html')

def terminos_y_condiciones(request):
    return render(request, 'principal/terminos_y_condiciones.html')
