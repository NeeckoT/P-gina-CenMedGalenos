from django.db import models

class Afp(models.Model):
    class Meta:
        db_table = 'Afp'
    id_afp = models.IntegerField(primary_key=True)
    afp = models.CharField(max_length=50)
    descuento_afp = models.IntegerField()

class Atencion(models.Model):
    ate_id = models.IntegerField(primary_key=True)
    fecha_atencion = models.DateField()
    hr_atencion = models.CharField(max_length=5)
    costo = models.IntegerField()
    medico_med_run = models.IntegerField()
    pac_run = models.IntegerField()
    hora_id_hora = models.IntegerField()
    centro_medico_id_centro_medico = models.IntegerField(null=True)

class Cargo(models.Model):
    car_id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)

class CentroMedico(models.Model):
    id_centro_medico = models.IntegerField(primary_key=True)
    centro_medico = models.CharField(max_length=50)
    fono_centro = models.IntegerField()
    direccion_id_direccion = models.IntegerField(null=True)

class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    comuna = models.CharField(max_length=50)

class DetalleAtenMedicasMensuales(models.Model):
    mes_anno_atencion = models.CharField(max_length=7)
    atencion_ate_id = models.IntegerField(primary_key=True)
    paciente = models.CharField(max_length=100)
    sistema_salud_paciente = models.CharField(max_length=100)
    descrip_sistema_salud = models.CharField(max_length=100)
    costo_atencion = models.IntegerField()

class Direccion(models.Model):
    id_direccion = models.IntegerField(primary_key=True)
    direccion = models.CharField(max_length=100)
    comuna_id_comuna = models.IntegerField()

class Empleado(models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    rut_empleado = models.IntegerField()
    dv_empleado = models.CharField(max_length=1)
    nom_empleado = models.CharField(max_length=20)
    ap_empleado = models.CharField(max_length=20)
    fecha_contrato = models.DateField()
    telefono_empleado = models.IntegerField()
    correo_empleado = models.CharField(max_length=100)
    rol = models.CharField(max_length=20)
    rol_id_rol = models.IntegerField()
    sueldo_base = models.IntegerField()
    contraseña_empleado = models.CharField(max_length=50)
    prevision_salud_id_prevision = models.IntegerField()
    afp_id_afp = models.IntegerField()

class ErroresProceso(models.Model):
    id_error = models.IntegerField(primary_key=True)
    subprograma_error = models.CharField(max_length=150)
    descripcion_error = models.CharField(max_length=500)


class Especialidad(models.Model):
    esp_id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=25)

class Hora(models.Model):
    id_hora = models.IntegerField(primary_key=True)
    fecha_y_hora = models.DateField()
    paciente_pac_run = models.IntegerField(null=True)
    atencion_ate_id = models.IntegerField()
    especialidad_esp_id = models.IntegerField()

class Medico(models.Model):
    med_run = models.IntegerField(primary_key=True)
    dv_run = models.CharField(max_length=1)
    pnombre = models.CharField(max_length=15)
    snombre = models.CharField(max_length=15)
    apaterno = models.CharField(max_length=15)
    amaterno = models.CharField(max_length=15)
    telefono = models.IntegerField()
    sueldo_base = models.IntegerField()
    fecha_contrato = models.DateField()
    especialidad_esp_id = models.IntegerField()
    correo_medico = models.CharField(max_length=150)
    contraseña_medico = models.CharField(max_length=50)
    afp_id_afp = models.IntegerField()
    prevision_salud_id_prevision = models.IntegerField()
    descuento_sueldo_id_descuento1 = models.IntegerField(null=True)

class Paciente(models.Model):
    class Meta:
        db_table = 'Paciente'
    pac_run = models.IntegerField(primary_key=True)
    dv_run = models.CharField(max_length=1)
    pnombre = models.CharField(max_length=15)
    snombre = models.CharField(max_length=15)
    apaterno = models.CharField(max_length=15)
    amaterno = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    telefono = models.IntegerField()
    salud_sal_id = models.IntegerField(null=True)
    correo_paciente = models.CharField(max_length=150)
    contraseña_paciente = models.CharField(max_length=50)
    genero_paciente = models.CharField(max_length=5)
    direccion_id_direccion = models.IntegerField()

class PagoAtencion(models.Model):
    atencion_ate_id = models.IntegerField(primary_key=True)
    fecha_pago = models.DateField()
    valor_a_pagar = models.IntegerField()

class PrevisionSalud(models.Model):
    id_prevision = models.IntegerField(primary_key=True)
    prevision = models.CharField(max_length=50)
    descuento_prevision = models.IntegerField()

class Relation14(models.Model):
    hora_id_hora = models.IntegerField(primary_key=True)
    empleado_id_empleado = models.IntegerField()

class Relation15(models.Model):
    empleado_id_empleado = models.IntegerField(primary_key=True)
    pago_atencion_atencion_ate_id = models.IntegerField()

class ResumenAtenMedicasMensuales(models.Model):
    mes_anno_atencion = models.CharField(max_length=8, primary_key=True)
    total_aten_unid_ambul = models.IntegerField()
    total_aten_unid_urgen = models.IntegerField()
    total_aten_unid_pacritico = models.IntegerField()
    total_aten_unid_adulto = models.IntegerField()
    total_aten_unid_infantil = models.IntegerField()
    total_aten_unid_maternidad = models.IntegerField()
    total_aten_unid_cirugia = models.IntegerField()
    total_aten_unid_cirugia_plast = models.IntegerField()
    total_aten_unid_sobrep_obes = models.IntegerField()
    fecha_grabacion = models.DateField()

class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=1000)

class Salud(models.Model):
    sal_id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    costo_pago = models.IntegerField()
    tipo_salud_tipo_sal_id = models.CharField(max_length=3)

class TipoSalud(models.Model):
    tipo_sal_id = models.CharField(max_length=3, primary_key=True)
    descripcion = models.CharField(max_length=100)