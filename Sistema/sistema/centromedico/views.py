from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

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



@permission_required('centromedico.view_hora')
def secretaria_horas(request):

    horas = Hora.objects.all()

    data = {
        'horas': horas,
        'formhora': HoraForm()
    }

    if request.method == 'POST':
        formulario = HoraForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "¡Guardado correctamente!"
        else:
            data["formhora"] = formulario

    return render(request, 'secretaria/horas.html', data)


@permission_required('centromedico.change_hora')
def secretaria_modificar_horas(request, id):

    hora = get_object_or_404(Hora, id_hora = id)

    data = {
        'formhora': HoraForm( instance = hora)
    }

    if request.method == 'POST':
        formulario = HoraForm(data = request.POST, instance = hora)
        if formulario.is_valid():
            formulario.save()
            return redirect(to = "s_horas")
        data["formhora"] = formulario

    return render(request, 'secretaria/modhoras.html', data)

@permission_required('centromedico.delete_hora')
def secretaria_eliminar_horas (request, id):
    hora = get_object_or_404(Hora, id_hora = id)
    hora.delete()
    return redirect(to = "s_horas")






def registro(request):

    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"],
            password =formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to = "/")

    return render(request, 'registration/registro.html', data)





def paciente_agendar_hora(request):

    horas = Hora.objects.all()

    data = {
        'horas': horas,
    }

    return render(request, 'pacientes/agendarhora.html', data)




def paciente_confirmar_horas(request, id):

    hora = get_object_or_404(Hora, id_hora = id)

    data = {
        'hora':hora,
        'formhora': ConfirmarHoraForm( instance = hora)
    }

    if request.method == 'POST':
        formulario = ConfirmarHoraForm(data = request.POST, instance = hora)
        if formulario.is_valid():
            hora.agendado = True
            formulario.save()
            messages.success(request, (f"La hora {hora.fecha_y_hora} se ha agendado correctamente"))
            return redirect(to = "agendar")
        messages.error(request, ("Ha ocurrido un error, por favor intenta más tarde."))
        data["formhora"] = formulario

    return render(request, 'pacientes/confirmaagendahora.html', data)
