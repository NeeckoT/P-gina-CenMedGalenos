# Generated by Django 4.2.7 on 2023-11-24 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('centromedico', '0014_alter_hora_medico_med_run_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hora',
            name='especialidad_esp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centromedico.especialidad'),
        ),
        migrations.AlterField(
            model_name='hora',
            name='medico_med_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centromedico.medico'),
        ),
        migrations.AlterField(
            model_name='hora',
            name='paciente_pac_run',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='centromedico.paciente'),
        ),
    ]
