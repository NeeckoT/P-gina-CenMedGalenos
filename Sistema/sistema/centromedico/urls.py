from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('pacientes', views.pacientes, name='pacientes'),
    path('pacientes/crear', views.registrarUsuario, name='crear'),
    path('pacientes/editar', views.editarUsuario, name='editar'),
    path('pacientes/eliminar/<int:rut>/', views.eliminarUsuario, name='eliminar'),
    path('horamedico', views.horamedico, name='horamedico'),
    path('horamedico/crear', views.registrarHora, name='crearHora'),
    path('horamedico/editar', views.editarHora, name='editarHora'),
    path('horamedico/eliminar/<int:rut>/', views.eliminarHora, name='eliminarHora'),
    path('ListaPacientesAtencion/Lista', views.ListaPacientes, name='Lista'),
    path('crear_datos_completos/', views.generar_horas, name='Datos_completos'),
    path('CRUD/', views.crud, name='CRUD'),

]
