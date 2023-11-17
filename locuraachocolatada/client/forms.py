from django import forms
from client.models import *

class categoriaForm(forms.ModelForm):
    class Meta:
        model= Categoria
        fields=['nombre']
        widgets={
            'nombre':forms.TextInput(label='Ingrese el nombre de la cátegoria a agregar.',placeholder='Escriba el nombre de la categoria', attrs={'class':"label-forms"})
        }
class productosForm (forms.ModelForm):
    class Meta:
        model= Producto
        fields=['nombre','descripcion','precio','oferta','descuento_oferta','categoria']
        widgets={
            'nombre':forms.TextInput(label='Ingrese el nombre del producto.', placeholder='Nombre producto', attrs={'class':'label-forms'}),
            'descipcion':forms.NumberInput(label='Ingrese la descripción del producto.',placeholder='Ingrese una breve descripción del producto',attrs={'class':'label-forms'}),
            'precio':forms.TextInput(label='Ingrese el precio del producto.',placeholder='Precio producto',attrs={'class':'label-forms'}),
            'descuento_oferta':forms.NumberInput(label='Ingrese el descuento si es que aplica la oferta.',placeholder='Porcentaje del descuento',attrs={'class':'label-forms'}),
            'categoria':forms.ModelChoiceField(queryset=Categoria.objects.all(),empty_label="Categoria del producto", label="Escoja una categoria para el producto")
            
        }
        oferta:forms.TypedChoiceField(coerce=lambda x : x==True,choices=((True,'Si'),(False,'No')), widget=forms.RadioSelect, label='¿El producto se encuentra en oferta?')