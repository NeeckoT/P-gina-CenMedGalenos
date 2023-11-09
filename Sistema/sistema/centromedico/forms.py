from django import forms
from .models import Usuario
from .models import HorasAtencionMedico


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class HorasAtencionMedicoForm(forms.ModelForm):
    class Meta:
        model = HorasAtencionMedico
        fields = '__all__'  
        widgets = {
            'fec_hr_ini': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fec_hr_ter': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }