from django import forms
from .models import Hora, Medico, Especialidad
from .models import Paciente
from .models import Atencion
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

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = '__all__'

class CustomForm(forms.Form):
    medico = MedicoForm()
    hora = HoraForm()
    especialidad = EspecialidadForm()
