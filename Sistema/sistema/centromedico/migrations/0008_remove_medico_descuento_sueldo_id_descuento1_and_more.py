# Generated by Django 4.2.7 on 2023-11-23 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centromedico', '0007_afp_atencion_cargo_centromedico_comuna_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medico',
            name='descuento_sueldo_id_descuento1',
        ),
        migrations.AddField(
            model_name='hora',
            name='medico_med_run',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hora',
            name='fecha_y_hora',
            field=models.DateTimeField(),
        ),
        migrations.AlterModelTable(
            name='afp',
            table='Afp',
        ),
        migrations.AlterModelTable(
            name='medico',
            table='Medico',
        ),
        migrations.AlterModelTable(
            name='paciente',
            table='Paciente',
        ),
    ]
