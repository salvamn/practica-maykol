from django.db import models

# Create your models here.
class Institucion(models.Model):
    nombre = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=150)
    region = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.nombre