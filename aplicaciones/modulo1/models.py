from django.db import models

# Create your models here.
class Entidad(models.Model):
	nombre = models.CharField(max_length=100)
	observacion = models.TextField()
	fecha_creacion = models.DateField() 
	fecha_destino = models.DateTimeField(auto_now=True)
	archivo = models.FileField(upload_to = 'files/', blank = True, null = True)
	estado = models.BooleanField(default=True)

class Prueba(models.Model):
	text = models.CharField(max_length=100)
	estado = models.BooleanField(default=True)