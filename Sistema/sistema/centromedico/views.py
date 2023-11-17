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







def generar_horas(request):
    if request.method == 'POST':
        form = GenerarHorasForm(request.POST)
        if form.is_valid():
            med_run = form.cleaned_data['med_run']
            dv_run = form.cleaned_data['dv_run']
            esp_id = form.cleaned_data['esp_id']

            # Aquí puedes generar las horas para el médico utilizando los datos proporcionados
            # Puedes crear instancias de Hora y guardarlas en la base de datos

            return redirect('inicio')  # Redirige a una página de éxito o donde desees
    else:
        form = GenerarHorasForm()

    return render(request, 'ListaPacientesAtencion/Lista.html', {'form': form})




def crud(request):
    context = {}
    form = MedicoForm()
    medicos = Medico.objects.all()
    context['medicos'] = medicos

    if request.method == 'POST':
        if 'save' in request.POST:
            form = MedicoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('CRUD')
            else:
                form = MedicoForm()
                context['form_error'] = "Error: El formulario no es válido. Por favor, corrige los errores a continuación."

    context['form'] = form
    return render(request, 'CRUD/CRUD.html', context)



