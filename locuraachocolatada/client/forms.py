from django import forms
from client.models import *

class categoriaForm(forms.ModelForm):
    class Meta:
        model= Categoria
        fields=['nombre']
        widgets={
            'nombre':forms.TextInput(attrs={'class':"label-forms",'label':'Ingrese el nombre de la cátegoria a agregar.','placeholder':'Escriba el nombre de la categoria'})
        }
class productosForm (forms.ModelForm):
    class Meta:
        model= Producto
        fields=['nombre','descripcion','precio','descuento_oferta','categoria','imagen']
        widgets={
            'nombre':forms.TextInput(attrs={'class':'label-forms','label':'Ingrese el nombre del producto.', 'placeholder':'Nombre producto'}),
            'descripcion':forms.Textarea(attrs={'class':'label-forms','label':'Ingrese la descripción del producto.','placeholder':'Ingrese una breve descripción del producto'}),
            'precio':forms.NumberInput(attrs={'class':'label-forms','label':'Ingrese el precio del producto.','placeholder':'Precio producto'}),
            'descuento_oferta':forms.NumberInput(attrs={'class':'label-forms','label':'Ingrese el descuento si es que aplica la oferta.','placeholder':'Porcentaje del descuento'}),
            'categoria':forms.Select(attrs={'label':"Escoja una categoria para el producto"}),
            'imagen':forms.ClearableFileInput(attrs={'class': 'label-forms', 'placeholder': 'Sube la imagen del producto'}),
            'oferta': forms.RadioSelect(),
            'popular': forms.BooleanField(),
        }