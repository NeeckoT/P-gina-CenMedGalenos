# Generated by Django 4.2.7 on 2023-11-10 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centromedico', '0005_horasatencionmedico_rut_dv_medico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horasatencionmedico',
            name='fec_hr_ter',
        ),
    ]
