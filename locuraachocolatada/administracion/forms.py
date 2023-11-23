from django import forms
from client.models import *
from administracion.models import *
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class productoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields='__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class':'form-control'}),
            'oferta': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'descuento_oferta': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'popular': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
class categoriaForm(forms.ModelForm):
    class Meta:
        model= Categoria
        fields=['nombre']
        widgets={
            'nombre':forms.TextInput(attrs={'class':"label-forms",'label':'Ingrese el nombre de la cátegoria a agregar.','placeholder':'Escriba el nombre de la categoria'})
        }
class DescripcionEmpresaForm(forms.ModelForm):
    class Meta:
        model = descripcionEmpresa
        exclude = ['id']
        widgets = {
            'sobre_nosotros': forms.Textarea(attrs={'class': 'form-control'}),
            'descripcion_prductos': forms.Textarea(attrs={'class': 'form-control'}),
            'terminos_y_condiciones': forms.Textarea(attrs={'class': 'form-control'}),
            'horario_atencion': forms.TextInput(attrs={'class': 'form-control'}),
            'nro_whatsapp': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_contacto': forms.EmailInput(attrs={'class': 'form-control'}),
            'username_instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'enlace_instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'username_facebook': forms.TextInput(attrs={'class': 'form-control'}),
            'enlace_facebook': forms.TextInput(attrs={'class': 'form-control'}),
        }

