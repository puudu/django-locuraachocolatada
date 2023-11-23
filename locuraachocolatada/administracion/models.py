from django.db import models
from django.contrib.auth import get_user_model
from client.models import Producto

class auditoriaProductos(models.Model):
    
    accion=models.CharField(max_length=15,)
    fecha= models.DateField(auto_now_add=True)
    usuario= models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    producto_modificado=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.accion} - {self.producto_modificado} - {self.fecha}'