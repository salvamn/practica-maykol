# Generated by Django 4.2.6 on 2023-12-10 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcatastro', '0017_alter_catastroambulancias_id_convenio_mantenimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catastroambulancias',
            name='costo_anual_mantenimiento',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]