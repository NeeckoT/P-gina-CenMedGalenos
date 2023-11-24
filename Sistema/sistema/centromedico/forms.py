from django import forms
from tempus_dominus.widgets import DatePicker
from .models import Hora, Medico, Especialidad
from .models import Paciente
from .models import Atencion

from django.contrib.auth.forms import UserCreationForm
#from .models import Usuario
#from .models import HorasAtencionMedico


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

class ListaPaciente(forms.ModelForm):
    class Meta:
        model = Atencion
        fields= '__all__'






class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'

class HoraForm(forms.ModelForm):
    class Meta:
        model = Hora
        fields = '__all__'

class ConfirmarHoraForm(forms.ModelForm):
    paciente_pac_run = forms.IntegerField()
    class Meta:
        model = Hora
        fields = ['paciente_pac_run']

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    pass