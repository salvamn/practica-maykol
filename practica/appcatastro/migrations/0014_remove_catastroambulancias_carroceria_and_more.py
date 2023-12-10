# Generated by Django 4.2.6 on 2023-12-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcatastro', '0013_alter_catastroambulancias_kilometraje'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catastroambulancias',
            name='carroceria',
        ),
        migrations.RemoveField(
            model_name='catastroambulancias',
            name='clase',
        ),
        migrations.RemoveField(
            model_name='catastroambulancias',
            name='id_convenio',
        ),
        migrations.RemoveField(
            model_name='catastroambulancias',
            name='propietario',
        ),
        migrations.RemoveField(
            model_name='catastroambulancias',
            name='sub_ubicacion',
        ),
        migrations.RemoveField(
            model_name='catastroambulancias',
            name='ubicacion',
        ),
        migrations.AddField(
            model_name='catastroambulancias',
            name='anio_ingreso_plan_mantenimiento',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='catastroambulancias',
            name='clase_ambulancia',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='catastroambulancias',
            name='costo_anual_mantenimiento',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='catastroambulancias',
            name='establecimineto',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='catastroambulancias',
            name='estado_situacion',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='catastroambulancias',
            name='id_convenio_mantenimiento',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='catastroambulancias',
            name='nombre_proveedor',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='catastroambulancias',
            name='region',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='catastroambulancias',
            name='tipo_ambulancia',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='catastroambulancias',
            name='tipo_carroceria',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='catastroambulancias',
            name='tipo_mantenimiento',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='catastroambulancias',
            name='vida_util_residual',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='catastroambulancias',
            name='criticidad',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='catastroambulancias',
            name='eliminado',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='catastroambulancias',
            name='estado',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='catastroambulancias',
            name='funcion',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='catastroambulancias',
            name='garantia',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='catastroambulancias',
            name='kilometraje',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='catastroambulancias',
            name='marca',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='catastroambulancias',
            name='modelo',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='catastroambulancias',
            name='numero_motor',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='catastroambulancias',
            name='patente',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='catastroambulancias',
            name='plan_mantencion',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='catastroambulancias',
            name='samu',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='catastroambulancias',
            name='tipo_equipo',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='catastroambulancias',
            name='vencimiento_garantia',
            field=models.DateField(),
        ),
    ]
