from django.db import models

# Create your models here.

class CatastroEquipoIndustriales(models.Model):
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
    
    
class CatastroEquiposMedicos(models.Model):
    ubicacion = models.CharField(max_length=100)
    sub_ubicacion = models.CharField(max_length=100)
    clase = models.CharField(max_length=50)
    sub_clase = models.CharField(max_length=70)
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    serie = models.CharField(max_length=100)
    numero_inventario = models.CharField(max_length=100)
    anio = models.IntegerField()
    vida_util = models.IntegerField()
    propietario = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    criticidad = models.CharField(max_length=100)
    garantia = models.IntegerField()
    vencimiento_garantia = models.CharField(max_length=100)
    plan_mantencion = models.IntegerField()
    tipo_equipo = models.CharField(max_length=100)
    id_convenio = models.IntegerField()
    id_institucion = models.IntegerField()
    eliminado = models.IntegerField()
        
    
class CatastroAmbulancias(models.Model):
    ubicacion = models.CharField(max_length=100)
    sub_ubicacion = models.CharField(max_length=100)
    carroceria = models.CharField(max_length=100)
    clase = models.CharField(max_length=50)
    samu = models.CharField(max_length=4)
    funcion = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    patente = models.CharField(max_length=50)
    numero_motor = models.CharField(max_length=100)
    kilometraje = models.IntegerField()
    propietario = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    anio = models.IntegerField()
    vida_util = models.IntegerField()
    criticidad = models.CharField(max_length=100)
    garantia = models.IntegerField()
    vencimiento_garantia = models.CharField(max_length=100)
    plan_mantencion = models.IntegerField()
    tipo_equipo = models.CharField(max_length=100)
    id_convenio = models.IntegerField()
    id_institucion = models.IntegerField()
    eliminado = models.IntegerField()
    
    