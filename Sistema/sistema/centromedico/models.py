from django.db import models

class Usuario(models.Model):
    rut = models.IntegerField(primary_key=True)  # Definición de rut como clave primaria
    rut_dv = models.CharField(max_length=1)
    nombre_1 = models.CharField(max_length=20)
    nombre_2 = models.CharField(max_length=20)
    apellido_1 = models.CharField(max_length=20)
    apellido_2 = models.CharField(max_length=20)
    correo = models.EmailField(max_length=25)
    fono = models.IntegerField(default=0)
    salud = models.IntegerField(default=0)
    contrasena = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre_1} {self.apellido_1}"


class HorasAtencionMedico(models.Model):
    rut_medico = models.IntegerField(primary_key=True)
    rut_dv_medico = models.CharField(max_length=1, default='0')  # Se agrega el campo rut_dv_medico con un valor predeterminado de '0'
    fec_hr_ini = models.DateTimeField()  # Fecha y hora de inicio de la consulta
    fec_hr_ter = models.DateTimeField()  # Fecha y hora de término de la consulta
    nombre_medico = models.CharField(max_length=100)
    apellido_medico = models.CharField(max_length=100)
    especialidad = models.IntegerField()

    def __str__(self):
        return f'{self.rut_medico} - {self.nombre_medico} {self.apellido_medico}'



