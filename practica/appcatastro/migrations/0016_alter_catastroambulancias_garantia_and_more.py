# Generated by Django 4.2.6 on 2023-12-09 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcatastro', '0015_rename_establecimineto_catastroambulancias_establecimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catastroambulancias',
            name='garantia',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='catastroambulancias',
            name='vencimiento_garantia',
            field=models.CharField(max_length=150),
        ),
    ]
