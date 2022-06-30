from ast import Delete
from django.db import models

# Create your models here.


class contacto(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=200, verbose_name="Nombres")
    telefono = models.TextField(verbose_name="Teléfono", null=True)
    image = models.ImageField(upload_to='imagenes/',verbose_name="Imagen",null=True )
    def __str__(self):
        fila = "Nombre: " + self.nombres + " - " + "Teléfono:" + self.telefono
        return fila

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)    
        super().delete()       


