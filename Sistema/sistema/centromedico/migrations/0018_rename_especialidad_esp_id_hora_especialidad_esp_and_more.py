# Generated by Django 4.2.7 on 2023-11-24 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centromedico', '0017_rename_especialidad_esp_id_id_hora_especialidad_esp_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hora',
            old_name='especialidad_esp_id',
            new_name='especialidad_esp',
        ),
        migrations.RenameField(
            model_name='hora',
            old_name='medico_med_run_id',
            new_name='medico_med_run',
        ),
        migrations.RenameField(
            model_name='hora',
            old_name='paciente_pac_run_id',
            new_name='paciente_pac_run',
        ),
    ]