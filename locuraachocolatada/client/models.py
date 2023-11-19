from django.db import models

class Categoria (models.Model):
    nombre= models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombre

class Producto (models.Model):
    nombre= models.CharField(max_length=10)
    descripcion= models.TextField()
    precio= models.IntegerField()
    oferta=models.BooleanField(null=True, blank=True)
    descuento_oferta=models.IntegerField(null=True,blank=True)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='img/productos/',null=False, default='img/productos/default_image.jpg')
    popular = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.nombre
    
class descripcionEmpresa(models.Model):
    sobre_nosotros= models.TextField()
    descripcion_prductos=models.TextField()
    terminos_y_condiciones=models.TextField()