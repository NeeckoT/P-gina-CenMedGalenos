# Generated by Django 3.2.8 on 2023-11-07 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centromedico', '0003_horasatencionmedico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horasatencionmedico',
            name='rut_medico',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
