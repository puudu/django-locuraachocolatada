from django.db import models

class Categoria (models.Model):
    nombre= models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombre

class Producto (models.Model):
    nombre= models.CharField(max_length=30)
    descripcion= models.TextField()
    precio= models.IntegerField()
    oferta=models.BooleanField(null=True, blank=True)
    descuento_oferta=models.IntegerField(null=True,blank=True)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen=models.ImageField(null=True, upload_to='productos/imagenes')
    popular = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.nombre
    
class descripcionEmpresa(models.Model):
    sobre_nosotros= models.TextField(default='')
    descripcion_prductos=models.TextField(default='')
    terminos_y_condiciones=models.TextField(default='')
    horario_atencion = models.CharField(max_length=120,default='')
    nro_whatsapp = models.CharField(max_length=12,default='')
    correo_contacto = models.EmailField(default='')
    username_instagram = models.CharField(max_length=60,default='')
    enlace_instagram = models.CharField(max_length=120,default='')
    username_facebook = models.CharField(max_length=60,default='')
    enlace_facebook = models.CharField(max_length=120,default='')