# Generated by Django 4.2.6 on 2023-10-29 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appinstituciones', '0001_initial'),
        ('appautenticacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='institucion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appinstituciones.institucion'),
        ),
    ]
