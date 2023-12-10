from django.db import models

# Create your models here.

class CatastroEquipoIndustriales(models.Model):
    nombre_recinto = models.CharField(max_length=150, default='')
    ubicacion = models.CharField(max_length = 150, default='')
    clase = models.CharField(max_length = 150, default='')
    subclase = models.CharField(max_length = 150, default='')
    nombre = models.CharField(max_length = 150, default='')
    marca = models.CharField(max_length = 150, default='')
    modelo = models.CharField(max_length = 150, default='')
    serie = models.CharField(max_length = 150, default='')
    numero_inventario = models.CharField(max_length = 150, default='')
    anio = models.IntegerField(default=0)
    vida_util = models.IntegerField(default=0)
    vida_util_residual = models.IntegerField(default=0)
    estado = models.CharField(max_length = 150, default='')
    criticidad = models.CharField(max_length = 150, default='')
    garantia = models.CharField(max_length = 150, default='')
    vencimiento_garantia = models.CharField(max_length = 150, default='')
    plan_mantencion = models.CharField(max_length = 150, default='')
    anio_ingreso_plan_mantenimiento = models.IntegerField(default=0)
    tipo_mantenimiento = models.CharField(max_length = 150, default='')
    nombre_proveedor = models.CharField(max_length = 150, default='')
    id_convenio_mantenimiento = models.CharField(max_length = 150, default='')
    costo_anual_mantenimiento = models.IntegerField(default=0)
    tipo_equipo = models.CharField(max_length = 150, default='')
    id_institucion = models.IntegerField()
    eliminado = models.IntegerField(default=0)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    # servicio_clinico = models.CharField(max_length=200, blank=True)
    # recinto = models.CharField(max_length=100, blank=True)
    # clase = models.CharField(max_length=100, blank=True)
    # subclase = models.CharField(max_length=100, blank=True)
    # nombre_equipo = models.CharField(max_length=100, blank=True)
    # marca = models.CharField(max_length=100, blank=True)
    # modelo = models.CharField(max_length=100, blank=True)
    # serie = models.CharField(max_length=100, blank=True)
    # numero_inventario = models.CharField(max_length=100, blank=True)
    # anio_adquisicion = models.CharField(max_length=100, blank=True)
    # vida_util = models.IntegerField(null=True)
    # vida_util_residual = models.IntegerField(null=True)
    # propio = models.CharField(max_length=50, blank=True) # Propio - Arriendo Comodato
    # estado = models.CharField(max_length=50, blank=True) # Bueno - Regular - Malo - Baja
    # garantia = models.CharField(max_length=50, blank=True) # Si - No
    # anio_vencimiento_garantia = models.IntegerField(null=True)
    # bajo_plan_mantenimiento = models.CharField(max_length=50, blank=True) # Si - No
    # id_institucion = models.IntegerField(null=True)
    
    
class CatastroEquiposMedicos(models.Model):
    servicio_clinico = models.CharField(max_length = 150, default='')
    recinto = models.CharField(max_length = 150, default='')
    clase = models.CharField(max_length = 150, default='')
    subclase = models.CharField(max_length = 150, default='')
    nombre = models.CharField(max_length = 150, default='')
    marca = models.CharField(max_length = 150, default='')
    modelo = models.CharField(max_length = 150, default='')
    serie = models.CharField(max_length = 150, default='')
    numero_inventario = models.CharField(max_length = 150, default='')
    anio = models.IntegerField(default=0)
    vida_util = models.IntegerField(default=0)
    vida_util_residual = models.IntegerField(default=0)
    estado = models.CharField(max_length = 150, default='')
    criticidad = models.CharField(max_length = 150, default='')
    garantia = models.CharField(max_length = 150, default='')
    vencimiento_garantia = models.CharField(max_length = 150, default='')
    plan_mantencion = models.CharField(max_length = 150, default='')
    anio_ingreso = models.IntegerField(default=0)
    tipo_mantenimiento = models.CharField(max_length = 150, default='')
    nombre_proveedor = models.CharField(max_length = 150, default='')
    id_convenio = models.CharField(max_length = 150, default='')
    costo_anual = models.IntegerField(default=0)
    tipo_equipo = models.CharField(max_length = 150, default='')
    id_institucion = models.IntegerField()
    eliminado = models.CharField(max_length = 150, default='')
    
        
    
class CatastroAmbulancias(models.Model):
    region = models.CharField(max_length = 150, default = '')
    establecimiento = models.CharField(max_length = 150, default = '')
    tipo_carroceria = models.CharField(max_length = 150, default = '')
    tipo_ambulancia = models.CharField(max_length = 150, default = '')
    clase_ambulancia = models.CharField(max_length = 150, default = '')
    samu = models.CharField(max_length = 10) # Si - No
    funcion = models.CharField(max_length = 150)
    marca = models.CharField(max_length = 150)
    modelo = models.CharField(max_length = 150)
    patente = models.CharField(max_length = 150)
    numero_motor = models.CharField(max_length = 150)
    kilometraje = models.IntegerField()
    estado_situacion = models.CharField(max_length = 150, default = '')
    estado = models.CharField(max_length = 150) # Bueno - Regular - Malo - Baja
    anio = models.IntegerField()
    vida_util = models.IntegerField()
    vida_util_residual = models.IntegerField(default = 0)
    criticidad = models.CharField(max_length = 150)
    garantia = models.CharField(max_length = 150)
    vencimiento_garantia = models.CharField(max_length = 150)
    plan_mantencion = models.CharField(max_length = 150)
    anio_ingreso_plan_mantenimiento = models.IntegerField(default = 0)
    tipo_mantenimiento = models.CharField(max_length = 150, default = '')
    nombre_proveedor = models.CharField(max_length = 150, default = '')
    id_convenio_mantenimiento = models.CharField(max_length = 150)
    costo_anual_mantenimiento = models.IntegerField(default = 0)
    tipo_equipo = models.CharField(max_length = 150)
    id_institucion = models.IntegerField()
    eliminado = models.CharField(max_length = 150) # Si - No
