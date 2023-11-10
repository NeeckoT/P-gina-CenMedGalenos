from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *




def inicio(request):
    return render(request, 'paginas/inicio.html')    

def nosotros(request):
    return render(request, 'paginas/nosotros.html')    
#creacion de usuarios empleados/pacientes
def pacientes(request):
    usuarios = Paciente.objects.all()
    return render(request, 'pacientes/index.html',{'usuarios':usuarios})    

def registrarUsuario(request):
    formulario = UsuarioForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('inicio')
    return render(request, 'pacientes/crear.html', {'formulario': formulario})     

def editarUsuario(request):
    return render(request, 'pacientes/editar.html')     

def eliminarUsuario(request,rut):
    usuarios = Paciente.objects.get(rut=rut)
    usuarios.delete()
    return redirect('pacientes')
#creacion de horarios medicos
def horamedico(request):
    horas = Hora.objects.all()
    return render(request, 'horamedico/index.html',{'horas':horas})    

def registrarHora(request):
    formularioHora = HorasAtencionMedicoForm(request.POST or None)
    if formularioHora.is_valid():
        formularioHora.save()
        return redirect('inicio')
    return render(request, 'horamedico/crear.html', {'formularioHora': formularioHora}) 

def editarHora(request):
    return render(request, 'horamedico/editar.html')     

def eliminarHora(request,rut):
    horasmedico = Hora.objects.get(rut=rut)
    horasmedico.delete()
    return redirect('horamedico')

def ListaPacientes(request):
    Atenciones = Atencion.objects.all()
    return render(request, 'ListaPacientesAtencion/Lista.html',{'Atenciones':Atenciones})