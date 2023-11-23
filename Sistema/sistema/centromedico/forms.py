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

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = '__all__'


class GenerarHorasForm(forms.Form):
    med_run = forms.IntegerField()
    dv_run = forms.CharField(max_length=1)
    esp_id = forms.IntegerField()
 
    def clean_med_run(self):
        med_run = self.cleaned_data.get('med_run')
        # Realiza la validación que necesites para med_run
        # Por ejemplo, asegúrate de que exista un médico con ese med_run
        if not Medico.objects.filter(med_run=med_run).exists():
            raise forms.ValidationError("No se encontró un médico con este med_run.")
        return med_run





class CustomUserCreationForm(UserCreationForm):
    pass