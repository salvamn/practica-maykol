from django.db import models

# Create your models here.

class CatastroEquipoMedico(models.Model):
    servicio_clinico = models.CharField(max_length=200)
    recinto = models.CharField(max_length=100)
    clase = models.CharField(max_length=100)
    subclase = models.CharField(max_length=100)
    nombre_equipo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    serie = models.CharField(max_length=100)
    numero_inventario = models.CharField(max_length=100)
    anio_adquisicion = models.CharField(max_length=100)
    vida_util = models.IntegerField()
    vida_util_residual = models.IntegerField()
    propio = models.CharField(max_length=50) # Propio - Arriendo Comodato
    estado = models.CharField(max_length=50) # Bueno - Regular - Malo - Baja
    garantia = models.CharField(max_length=2) # Si - No
    anio_vencimiento_garantia = models.IntegerField()
    bajo_plan_mantenimiento = models.CharField(max_length=2) # Si - No
    
    
