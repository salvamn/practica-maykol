# Generated by Django 4.2.6 on 2023-12-10 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcatastro', '0021_rename_numero_serie_catastroequiposmedicos_numero_inventario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catastroequipoindustriales',
            name='anio_adquisicion',
        ),
        migrations.RemoveField(
            model_name='catastroequipoindustriales',
            name='anio_vencimiento_garantia',
        ),
        migrations.RemoveField(
            model_name='catastroequipoindustriales',
            name='bajo_plan_mantenimiento',
        ),
        migrations.RemoveField(
            model_name='catastroequipoindustriales',
            name='nombre_equipo',
        ),
        migrations.RemoveField(
            model_name='catastroequipoindustriales',
            name='propio',
        ),
        migrations.RemoveField(
            model_name='catastroequipoindustriales',
            name='recinto',
        ),
        migrations.RemoveField(
            model_name='catastroequipoindustriales',
            name='servicio_clinico',
        ),
        migrations.AddField(
            model_name='catastroequipoindustriales',
            name='anio',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='catastroequipoindustriales',
            name='anio_ingreso_plan_mantenimiento',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='catastroequipoindustriales',
            name='costo_anual_mantenimiento',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='catastroequipoindustriales',
            name='criticidad',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='catastroequipoindustriales',
            name='eliminado',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='catastroequipoindustriales',
            name='id_convenio_mantenimiento',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='catastroequipoindustriales',
            name='nombre',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='catastroequipoindustriales',
            name='nombre_proveedor',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='catastroequipoindustriales',
            name='nombre_recinto',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='catastroequipoindustriales',
            name='plan_mantencion',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='catastroequipoindustriales',
            name='tipo_equipo',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='catastroequipoindustriales',
            name='tipo_mantenimiento',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='catastroequipoindustriales',
            name='ubicacion',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='catastroequipoindustriales',
            name='vencimiento_garantia',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='catastroequipoindustriales',
            name='clase',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='catastroequipoindustriales',
            name='estado',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='catastroequipoindustriales',
            name='garantia',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='catastroequipoindustriales',
            name='id_institucion',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='catastroequipoindustriales',
            name='marca',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='catastroequipoindustriales',
            name='modelo',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='catastroequipoindustriales',
            name='numero_inventario',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='catastroequipoindustriales',
            name='serie',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='catastroequipoindustriales',
            name='subclase',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='catastroequipoindustriales',
            name='vida_util',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='catastroequipoindustriales',
            name='vida_util_residual',
            field=models.IntegerField(default=0),
        ),
    ]