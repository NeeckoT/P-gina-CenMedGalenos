# Generated by Django 3.2.8 on 2023-11-05 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.IntegerField(primary_key=True, serialize=False)),
                ('rut_dv', models.CharField(max_length=1)),
                ('nombre_1', models.CharField(max_length=20)),
                ('nombre_2', models.CharField(max_length=20)),
                ('apellido_1', models.CharField(max_length=20)),
                ('apellido_2', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=25)),
                ('contrasena', models.CharField(max_length=10)),
            ],
        ),
    ]
